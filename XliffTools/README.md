# XliffTool

xliff工具，可以通过xliff生成xlsx文件，也可以通过xlsx文件写入到xliff文件

## Example
生成xlsx文件
python main.py -g '~/Desktop/Localizations' '~/Desktop'

or

python main.py -g '~/Desktop/Localizations/en.xliff' '~/Desktop'

同步到xlsx文件
python main.py -r '~/Desktop/XX.xlsx' '~/Desktop/Localizations'

or

python main.py -r '~/Desktop/XX.xlsx' '~/Desktop/Localizations/en.xliff'