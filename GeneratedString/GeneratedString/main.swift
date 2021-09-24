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

if FileManager.default.fileExists(atPath: folderPath) {
    filePaths = [folderPath]
} else {
    guard let subpaths = FileManager.default.subpaths(atPath: folderPath) else {
        print("当前目录")
        exit(0)
    }
    filePaths = subpaths
}

let swiftFilePaths = filePaths.filter(\.isSwiftFile)

print("filePaths:\(filePaths)")
print("swiftFilePaths:\(swiftFilePaths)")

print("-------------------GeneratedString--------------------")
