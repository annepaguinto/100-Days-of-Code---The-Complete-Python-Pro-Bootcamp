with open(r".\Input\Names\invited_names.txt", "r") as names:
    name_list = names.readlines()
    for name in name_list:
        name = name.strip()
        with open(r".\Input\Letters\starting_letter.txt", "r") as letter:
            letter_body = letter.read()
        with open(fr"Output\ReadyToSend\letter_for_{name}.txt", "w") as names:
            names.write(letter_body.replace("[name],", f"{name},"))
