label_text = "Chaiǐ panň"
print(f"uncoded text: {label_text}")
encoded_label = label_text.encode("utf-8")
print(f"encoded text: {encoded_label}")
decode_label = encoded_label.decode("utf-8")
print(f"decoded text: {decode_label}")