z = zipfile.ZipFile(OUTPUT, MODE, zipfile.ZIP_DEFLATED)
zipdir(PATH, z)
z.close()
