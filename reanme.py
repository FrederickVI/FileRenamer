import os

os.chdir(r"C:\Users\PC\Desktop\corey schafer\parsing and renaming of multiple files\solar system")

print(os.getcwd())

for f in os.listdir():
    f_name, f_ext = os.path.splitext(f)
    f_title, f_number = f_name.split("#")

    f_title = f_title.strip() 
    f_number = f_number.strip().zfill(2)

    new_name = '{}-{}{}'.format(f_number, f_title, f_ext)

    os.rename(f, new_name)