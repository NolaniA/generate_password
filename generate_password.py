import tkinter as tk
from tkinter import messagebox
import random
import string


# อักขระพิเศษที่อนุญาต
allowed_special_chars = "~`!@#$%^&*-_+=()[]|\\/:;\"\'< >,.?"
space_bar = "          "
uppercase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase="abcdefghijklmnopqrstuvwxyz"
number="0123456789"

# count_by_byte=r"[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F680-\U0001F6FF\U0001F700-\U0001F77F\U0001F780-\U0001F7FF\U0001F800-\U0001F8FF\U0001F900-\U0001F9FF\U0001FA00-\U0001FAFF\U00013000-\U0001342F]"

# อักขระพิเศษที่ไม่อนุญาต (ตัวอย่าง: ภาษาไทย, Emoji ฯลฯ)ๆ็่้๊๋์ ่ ี ้ ุ ู ิ ี ึ ื ่ ้ ๊ ็ ๋ _่ _้่้๊๋็์ะาิีึืุูาัำ่้๊๋็์ะาิีึืุูาัำ_้_่ะ ั ่
disallowed_chars = "กขคงจฉชซญฎฐฑฒณดตถทธนบปผฝพฟภมยรลวศษสหฬอฮะาำเแโใไๆあいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをんおあえおおおっていម្តយរបស់អ្នកបនស្លប់នចំពោះមុខខ្លឃ្មុំ។सचमेंतेरमाँभालूकेसामनेमर।媽死在了一隻熊面前。😍😂😄😃😀😊ßśš😉😘èéêëēėę😚😗😙ôöòóœøōõ😜😝😛😳😁àáâäæãåā😔😌😒😞😣žźż😢😭😪😥😬😮😈⒜⒝⒞⒟⒠⒡⒢⒣😧😦😟😲😵😴😎ᴬᴮᶜᴰᴱᶠᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾᵠᴿˁᵀᵁᵛᵂˣʸᶻ😷😋😆😖😤😡çćč😠😨😫😩𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫😓😅😰😐ᵃᵇᶜᵈᵉᶠᵍʰᶤʲᵏˡᵐᶰᵒᵖᵠʳˢᵗᵘᵛʷˣʸᶻ😕😶😇☺️😏😑🙃ñń🙄☹️🤐🤑🤒🤓🤔🤕🙁🙂🤗𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ🤣🤠🤥🤤🤢îïíīįì😽ÿ😻😸ł😺💋❣️💝ûüùúū💞💖💕🤧😼🥶️🥸🥲✡☆★✬🔯💫✿©℁‱℡✌️✇✂$¢¥£₤¤﷼￥〉】︹｛＞）«〈♜♛♙♘♣♦♯♬♫❆㏄㎞㎏℃℉ϟ☀☁☂❆❄卐卍💔💙💚✔❎〥☻☺⚤☠∭≋≹⊽⋢⓹➅Ⅸ➑ⅠⅲⅡₐ≎◒æaɪɜ:ⓚⓓĤĩΣχφ㊪しㅙ😖💁‍♀️🙎🧚‍♀️🧟‍♀️🔒🔏⏲🌞➿🔁🗼🇲🇽ʎʍʌʇɹɯʞɾᴉɥƃɟǝɔɐ⅄Λ∩┴Ԁ˥ʞſפℲƎƆ∀ㄥϛㄣƐᄅƖ\u0E48\u0E49\u0E4A\u0E4B\u0E4C\u0E4D\u0E30\u0E32\u0E34\u0E35\u0E36\u0E37\u0E38\u0E39\u0E31\u0E33"
def generate():
    while True:
            length = random.randint(int(length_minimum.get()), int(length_maximum.get()))
            char_pool = ""
            password = ""
            if var_upper.get():
                char_pool += uppercase
                password += random.choice(uppercase)
            if var_lower.get():
                char_pool += lowercase
                password += random.choice(lowercase)
            if var_number.get():
                char_pool += number
                password += random.choice(number)
            if var_special.get():
                char_pool += allowed_special_chars
                password += random.choice(allowed_special_chars)
            if var_special_invalid.get():
                if var_special_invalid_count.get():
                    for _ in range(int(count_invalid.get())):
                        password += random.choice(disallowed_chars)
                else:
                    char_pool += disallowed_chars
                    password += random.choice(disallowed_chars)
            if var_space_bar.get():
                char_pool += space_bar
                password += random.choice(space_bar)

            password += ''.join(random.choices(char_pool, k=length-len(password)))
            password_list = list(password)
            random.shuffle(password_list)
            return ''.join(password_list)

def generate_password():
    try:
        if not (var_upper.get() or var_lower.get() or var_number.get() or var_special.get() or var_special_invalid.get() or var_space_bar.get()):
            messagebox.showerror("Error", "กรุณาเลือกประเภทอักขระอย่างน้อย 1 ประเภท")
            return

        
        count = int(count_entry.get())
        passwords = [generate() for _ in range(count)]
        # ล้างกล่องข้อความแล้วแสดงผลรหัสผ่าน
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, "\n".join(passwords))

    except ValueError:
        messagebox.showerror("Error", "กรุณากรอกค่าตัวเลขที่ถูกต้อง")



def copy_to_clipboard():
    # ดึงข้อความจาก result_text
    result = result_text.get("1.0", tk.END)
    
    if result:
        # คัดลอกข้อความไปที่คลิปบอร์ด
        root.clipboard_clear()
        root.clipboard_append(result)
        # messagebox.showinfo("Copy", "ข้อความถูกคัดลอกไปยังคลิปบอร์ดแล้ว")
    else:
        messagebox.showerror("Error", "ไม่มีข้อความให้คัดลอก")

# สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("Password Generator")
frame_left = tk.Frame(root, width=50, height=400)
frame_left.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
label_left = tk.Label(frame_left, text="Password Generator", font=("Arial", 12))
label_left.pack(pady=10)
frame_right = tk.Frame(root, width=50, height=400)
frame_right.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
label_right = tk.Label(frame_right, text="Condition Password Generator", font=("Arial", 12))
label_right.pack(pady=10)


# root.geometry("400x500")


# Label และ Input ความยาวรหัสผ่าน
length_label = tk.Label(frame_right, text="ความยาวรหัสผ่านเริ่มต้น:")
length_label.pack(pady=5)
length_minimum = tk.Entry(frame_right)
length_minimum.pack(pady=5)
length_minimum.insert(0, "8")

# Label และ Input ความยาวรหัสผ่าน
length_label = tk.Label(frame_right, text="ความยาวรหัสผ่านสูงสุด:")
length_label.pack(pady=5)
length_maximum = tk.Entry(frame_right)
length_maximum.pack(pady=5)
length_maximum.insert(0, "8")

# Label และ Input จำนวนรหัสผ่าน
count_label = tk.Label(frame_right, text="จำนวนรหัสผ่าน:")
count_label.pack(pady=5)
count_entry = tk.Entry(frame_right)
count_entry.pack(pady=5)
count_entry.insert(0, "10")

# ตัวเลือกประเภทอักขระ
var_upper = tk.BooleanVar(value=False)
var_lower = tk.BooleanVar(value=False)
var_number = tk.BooleanVar(value=False)
var_special = tk.BooleanVar(value=False)
var_special_invalid = tk.BooleanVar(value=False)
var_special_invalid_count = tk.BooleanVar(value=False)
var_space_bar = tk.BooleanVar(value=False)

upper_check = tk.Checkbutton(frame_right, text="ตัวพิมพ์ใหญ่ (A-Z)", variable=var_upper)
upper_check.pack(pady=5)
lower_check = tk.Checkbutton(frame_right, text="ตัวพิมพ์เล็ก (a-z)", variable=var_lower)
lower_check.pack(pady=5)
number_check = tk.Checkbutton(frame_right, text="ตัวเลข (0-9)", variable=var_number)
number_check.pack(pady=5)
special_check = tk.Checkbutton(frame_right, text="อักขระพิเศษที่อนุญาติ (~`!@#$%^&*-_+=()[]|\\/:;\"\'< >,.?)", variable=var_special)
special_check.pack(pady=5)
special_check_invalid = tk.Checkbutton(frame_right, text="อักขระพิเศษที่ไม่อนุญาติ (ไม่ใช่ภาษาอังกฤษ, emoji, symbol)", variable=var_special_invalid)
special_check_invalid.pack(pady=5)
option_label = tk.Label(frame_right, text="เงื่อนไขเพิ่มเติม", font=("Arial", 12))
option_label.pack(pady=5)
special_check_invalid_count = tk.Checkbutton(frame_right, text="อักขระพิเศษที่ไม่อนุญาติจะแสดงตามจำนวนตัวอักษรที่ระบุ", variable=var_special_invalid_count)
special_check_invalid_count.pack(pady=5)
count_invalid = tk.Entry(frame_right)
count_invalid.pack(pady=5)
count_invalid.insert(0, "1")
space_bar_check = tk.Checkbutton(frame_right, text="ช่องว่าง (sapce bar)", variable=var_space_bar)
space_bar_check.pack(pady=5)

# ปุ่มสร้างรหัสผ่าน
generate_button = tk.Button(frame_right, text="สร้างรหัสผ่าน", command=generate_password)
generate_button.pack(pady=5)
# copy_button = tk.Button(frame_right, text="คัดลอกข้อความ", command=copy_to_clipboard)
# copy_button.pack(pady=5)

# กล่องแสดงผลรหัสผ่าน
result_text = tk.Text(frame_left, height=30, width=40)
result_text.pack()
copy_button = tk.Button(frame_left, text="คัดลอกข้อความ", command=copy_to_clipboard)
copy_button.pack(pady=5)

root.mainloop()

#demo : https://jam.dev/c/3911b148-ef8a-43fd-a003-e73f1233ad4c
# cd directory
# python generate_password.py
