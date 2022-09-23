from importlib.resources import path
import os
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element

def tag_uri_and_name(elem):
    if elem.tag[0] == "{":
        uri, ignore, tag = elem.tag[1:].partition("}")
    else:
        uri = None
        tag = elem.tag
    return uri, tag

# 查找xliff文件，并判断文件类型
def findXliff(path):
    if os.path.isdir(path):
        for filename in findAllFile(path):
            if checkXliff(filename):
                yield filename
    elif os.path.isfile(path):
        if checkXliff(path):
            yield path
        else:
            print("这不是一个xliff文件")
    else:
        print(f"这是一个特殊文件或者路径不存在,路径:{path}")


def findAllFile(path):
    for root, ds, fs in os.walk(path):
        for f in fs:
            fullname = os.path.join(root, f)
            yield fullname

# 判断文件是否为xliff
def checkXliff(path):
    file = os.path.splitext(path)
    fileName, type = file
    if type == ".xliff":
        return True
    else:
        return False


# 解析xliff
def parseXliffPath(path, lang, data):
    tree = ET.parse(path)
    xliff = tree.getroot()
    parseXliffQuick(xliff, lang, data)
     

# 快捷便利节点
def parseXliffQuick(xliff: Element, lang, data):
    url, tag = tag_uri_and_name(xliff)
    if url != None:
        url = "{" + url + "}"
    else:
        url = ""
    file = next(xliff.iter(f"{url}file"))
    target_language = file.attrib["target-language"]
    lang.append(target_language)

    for unit in xliff.iter(f"{url}trans-unit"):
        id, s, t = parseTransUnit(unit)
        value = data.get(id, {})
        value[target_language] = t
        data[id] = value



# 按节点来解析
def parseXliff(xliff: Element):
    for file in xliff:
        parseFile(file)


def parseFile(file: Element):
    source_language = file.attrib["source-language"]
    target_language = file.attrib["target-language"]
    print(f"source_language:{source_language}, target_language:{target_language}")
    for child in file:
        if "body" in child.tag:
            parseBody(child)


def parseBody(body: Element):
    for unit in body:
        parseTransUnit(unit)


def parseTransUnit(unit: Element):
    id = unit.attrib["id"]
    s, t = None, None
    for body in unit:
        source, target = parseTransBody(body)
        if source != None:
            s = source
        if target != None:
            t = target
    return id, s, t


def parseTransBody(body: Element):
    # 不转义string
    text = repr(body.text)
    if "source" in body.tag:
        return text, None
    elif "target" in body.tag:
        return None, text
    else:
        return None, None
    

def mergeTransDataToXliff(langData, transData, xliffPath):
    
    tree = ET.parse(xliffPath)
    xliff = tree.getroot()
    url, tag = tag_uri_and_name(xliff)
    ET.register_namespace('', url)
    if url != None:
        url = "{" + url + "}"
    else:
        url = ""

    file = next(xliff.iter(f"{url}file"))
    target_language = file.attrib["target-language"]
    if target_language not in langData:
        return

    for unit in xliff.iter(f"{url}trans-unit"):
        id, s, t = getTransUnit(unit)
        if t != None and id in transData:
            text = transData[id].get(target_language, "")
            t.text = f"{text}"
        
    tree.write(xliffPath, encoding="UTF-8")

    # with open(xliffPath, "r+") as f:
    #     content = f.read()
    #     f.seek(0, 0)
    #     f.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
    #     f.close()
    


def getTransUnit(unit: Element):
    id = unit.attrib["id"]
    s, t = None, None
    for body in unit:
        if "source" in body.tag:
            s = body
        elif "target" in body.tag:
            t = body
    return id, s, t