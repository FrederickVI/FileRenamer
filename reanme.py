import os

os.chdir(r"Your file path here!")

print(os.getcwd())

for f in os.listdir():
    f_name, f_ext = os.path.splitext(f)
    f_title, f_number = f_name.split("Split!")

    f_title = f_title.strip() 
    f_number = f_number.strip().zfill(2)

    new_name = '{}-{}{}'.format(f_number, f_title, f_ext)

    os.rename(f, new_name)
