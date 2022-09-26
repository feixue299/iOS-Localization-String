# XliffTool

xliff工具，可以通过xliff生成xlsx文件，也可以通过xlsx文件写入到xliff文件

## Example
生成xlsx文件

<code>python main.py -g '\~/Desktop/Localizations' '\~/Desktop'</code>

or

<code>python main.py -g '\~/Desktop/Localizations/en.xliff' '\~/Desktop'</code>

同步到xlsx文件
  
<code>python main.py -r '\~/Desktop/XX.xlsx' '\~/Desktop/Localizations'</code>

or

<code>python main.py -r '\~/Desktop/XX.xlsx' '\~/Desktop/Localizations/en.xliff'</code>
