//
//  main.swift
//  GeneratedString
//
//  Created by mac on 2021/9/23.
//

import Foundation

extension String {
    func isFileType(_ fileType: String) -> Bool {
        return hasSuffix(".\(fileType)")
    }
    
    var isSwiftFile: Bool { isFileType("swift") }
    var isMFile: Bool { isFileType("m") }
}

var args = CommandLine.arguments

print("-------------------GeneratedString--------------------")

guard args.count >= 2 else {
    print("请输入扫描目录或文件的路径")
    exit(0)
}

let folderPath = args[1]
print("扫描目录或文件的路径:\(folderPath)")

let filePaths: [String]

var isDirectory: ObjCBool = false

if FileManager.default.fileExists(atPath: folderPath, isDirectory: &isDirectory), !isDirectory.boolValue {
    filePaths = [folderPath]
} else {
    guard let subpaths = FileManager.default.subpaths(atPath: folderPath) else {
        print("当前目录")
        exit(0)
    }
    filePaths = subpaths
}

let swiftFilePaths = filePaths.filter(\.isSwiftFile)

func regexHandler(folderPath: String, filePath: String, writeFile: FileHandle) {
    guard let txt = try? String(contentsOfFile: "\(folderPath)/\(filePath)") else { return }
    let regex = "\"([^\n\r\"]+?)\".localized\\(\\)"
    
    guard let re = try? NSRegularExpression(pattern: regex, options: .caseInsensitive) else { return }
    let range = NSRange(location: 0, length: txt.count)
    
    let matchs = re.matches(in: txt, options: NSRegularExpression.MatchingOptions.reportProgress, range: range)
    matchs.forEach { result in
        let start = result.range.location
        let end = start + result.range.length
        let startIndex = txt.index(txt.startIndex, offsetBy: start)
        let endIndex = txt.index(txt.startIndex, offsetBy: end)
        let value = txt[startIndex..<endIndex]
        let key = value.replacingOccurrences(of: ".localized()", with: "")
        if let data = "\(key) = \(key);\n".data(using: .utf8) {
            writeFile.seekToEndOfFile()
            writeFile.write(data)
        }
        print("\(value)")
    }
}
let writeFilePath = "\(folderPath)/../Localized.string"
if FileManager.default.createFile(atPath: writeFilePath, contents: nil, attributes: nil), let fileHander = FileHandle(forUpdatingAtPath: writeFilePath) {
    print("文件创建成功")
    swiftFilePaths.forEach({ regexHandler(folderPath: folderPath, filePath: $0, writeFile: fileHander) })
} else {
    print("文件创建失败")
}

print("-------------------GeneratedString--------------------")
