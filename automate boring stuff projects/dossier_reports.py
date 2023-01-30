import os, shutil, openpyxl, PyPDF2, re, zlib, fnmatch
from pathlib import Path

working_dir = os.getcwd()
pdf_file = []
unseen = []
seen_PR_excel = []
# finding PO pdf in current working directory

for file in os.listdir(working_dir):
    if file.endswith(".pdf"):
        pdf_file.append(file)
    else:
        continue

# Creating folder for each PO with folder name as the PO name
for files in pdf_file:
    pos_dir = Path(working_dir) / files
    new_folder = Path(working_dir) / str(files[: len(files) - 4])
    os.makedirs(new_folder, exist_ok=True)
    shutil.copy(pos_dir, new_folder)

    # finding their PO's respective PR's
    excel_sheet = openpyxl.load_workbook("Bright Boadu-Dossiers.xlsx")
    sheet = excel_sheet.active
    for row in range(2, sheet.max_row + 1):
        if sheet.cell(row=row, column=3).value == int(files[: len(files) - 4]):
            PR_NO = sheet.cell(row=row, column=2).value
            seen_PR_excel.append(PR_NO)
            PR_dir = Path(os.getcwd()) / "PR"
            for file in PR_dir.glob(f"*{PR_NO}*"):
                shutil.copy(file, new_folder)

        else:
            continue

    folder_names = re.compile(r"^[0-9]+$")
    folders = []
    unseen = []
    for file in os.listdir(os.getcwd()):
        if folder_names.search(file):
            folders.append(file)
        else:
            continue

    for folder in folders:
        folder_path = Path(os.getcwd()) / folder
        if len(os.listdir(folder_path)) < 2:
            unseen.append(folder)
        else:
            continue

print(pdf_file)

manifest_path = Path(
    r"C:\Users\104535brbo\Desktop\manifest\Manifest\Manifest 2020 & 2021"
)
signed_manifest_path = Path(r"C:\Users\104535brbo\Desktop\manifest\Signed manifests")
manifest_list = []

for folders, subfolders, files in os.walk(manifest_path):
    for file in files:
        if file.endswith(".pdf"):
            manifest_list.append(os.path.join(folders, file))
        else:
            continue


po_strings = []
for file in pdf_file:
    po_strings.append(str("PO: " + file[:len(file) - 4]))
print(po_strings)


pos_with_manifest_not_signed = []
pos_with_signed_manifest = []
pos_with_no_signed_manifest = []
for po in po_strings:
    found_manifest = []
    for file_dir in manifest_list:
#finding manifest name
        try:
            pdf_file = open(file_dir, "rb")
            pdf_reader = PyPDF2.PdfFileReader(pdf_file, strict=False)
            total_page = pdf_reader.numPages
            for page in range(0, total_page):
                pdf_getpage = pdf_reader.getPage(page)
                pdf_extract = pdf_getpage.extractText()
                if po in pdf_extract:
                    found_manifest.append(file_dir)
                    print(file_dir)
                else:
                    continue
        except (
            PyPDF2.utils.PdfReadError,
            KeyError,
            ValueError,
            TypeError,
            NameError,
            zlib.error,
        ):

            pass
    print(found_manifest)
    not_found_manifest = []
    #finding signed manifest using the manifest name found from above
    try:
        shortest_manifest = min(found_manifest, key=len)
        shortest_manifest_path = Path(shortest_manifest)
        pos_with_manifest_not_signed.append(po)
        search_containing = shortest_manifest_path.stem
        key_search_containing = search_containing[:36]
        print(shortest_manifest)

        print(search_containing)
        print(key_search_containing)
        signed_manifest_found = []
        for folders, subfolders, files in os.walk(signed_manifest_path):
            for file in files:
                file_path = os.path.join(folders, file)
                if fnmatch.fnmatch(file_path, f"*{key_search_containing}*"):
                    signed_manifest_found.append(file_path)
                else:
                    continue

        for shortest_signed_manifest_found in signed_manifest_found:
            path_of_signed_manifest = Path(shortest_signed_manifest_found)
            pos_with_signed_manifest.append(po)
            new_folder = Path(r"C:\Users\104535brbo\Desktop\new dossiers") / po[4:]
            print('copying folder: ' + str(path_of_signed_manifest))
            print('destination folder: ' + str(new_folder))
            shutil.copy(path_of_signed_manifest, new_folder)
    except ValueError:
        pass

for pos in set(pos_with_manifest_not_signed): 
    if pos not in pos_with_signed_manifest:
        pos_with_no_signed_manifest.append(pos)
    else:
        continue

print("successfully done")
print("Task Completed successfully")

print(set(pos_with_signed_manifest))
print(set(pos_with_manifest_not_signed))
print(set(pos_with_no_signed_manifest))
