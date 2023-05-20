import sys
import docx2txt

result = docx2txt.process("file.docx")
print(result)
print(sys.getsizeof(result))
