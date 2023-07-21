import PyPDF2

file_path = r"D:\MLN\Question bank_122.pdf"
full_text = ""
with open(file_path, "rb") as pdf_file_handle:
    pdf_reader = PyPDF2.PdfReader(pdf_file_handle)

    for i in range(len(pdf_reader.pages)):
        page_obj = pdf_reader.pages[i]
        full_text += "\n" + page_obj.extract_text()

text_split = full_text.split("\n")
for i in range(len(text_split)):
    if (
        text_split[i].startswith("a ")
        or text_split[i].startswith("b ")
        or text_split[i].startswith("c ")
        or text_split[i].startswith("d ")
    ):
        key = text_split[i][0]
        ans = text_split[i][2:]
        text_split[i] = "#" + key + "~" + ans

with open("result.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(text_split))
