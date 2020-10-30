import sys
import docx
import lxml

# Encode entire article to unicode.


# get filepath
filepath = str(sys.argv[1])
print("filepath used: ", filepath)

# get document
dirty_doc = docx.Document(filepath)
print("document is " + str(len(dirty_doc.paragraphs)) + " paragraphs long")

# print paragraphs for viewing
print("PRE-CLEANING")
i=0
while i<len(dirty_doc.paragraphs):
    print("Paragraph ", str(i))
    print(dirty_doc.paragraphs[i].text)
    i+=1

# encode paragraphs to unicode

test_string = "ABCDE"
print('test_string: ')
print(test_string.encode('utf-8'))

encoded_paragraphs_utf16 = list(map(lambda para: para.text.encode('unicode_escape', ), dirty_doc.paragraphs))
# encoded_paragraphs_utf8 = map(lambda para: para.encode('utf-8', 'replace'), encoded_paragraphs_utf16)
# list(encoded_paragraphs_utf16)
print("ENCODED PARAGRAPHS")
j=0
while j<len(encoded_paragraphs_utf16):
    print("Paragraph ", str(j))
    print(str(encoded_paragraphs_utf16[j]))
    j+=1

decoded_paragraphs = list(map(lambda para: para.decode('unicode_escape'), encoded_paragraphs_utf16))

# print("DECODED PARAGRAPHS")
# # decoded_paragraphs = list(decoded_paragraphs)
# j=0

# while j < len(decoded_paragraphs):
#     print("DECODED Paragraph ", str(j))
#     print(decoded_paragraphs[j])
#     j+=1

# encoded_paragraphs_ascii = map(lambda para: para.text.encode('ascii', 'replace'), dirty_doc.paragraphs)

# Isolate left-to-right marks E2 80 8E and remove


