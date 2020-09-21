import cil

logo = cil.read_image('codeit_logo')
text = cil.read_image('codeit_text')

print('코드잇 로고:')
# logo를 디스플래이해 주세요
cil.utils.display(logo)
print('\n코드잇 텍스트:')
# text를 디스플래이해 주세요
cil.utils.display(text)
### 코드를 작성해 주세요 ###

# text를 색상 반전해서 inverted_text에 저장해 주세요
inverted_text = cil.processing.invert(text)
# logo와 text를 합성한 이미지를 merged_img에 저장해 주세요
merged_img = cil.processing.merge(logo, text)

print('\n색상 반전 텍스트:')
# inverted_text를 디스플래이해 주세요
cil.utils.display(inverted_text)
print('\n합성 이미지:')
cil.utils.display(merged_img)
### 코드를 작성해 주세요 ###

# 채점 코드
print()
key_functions = ['read_image', 'save_image', 'display', 'invert', 'merge']
non_key_functions = ['get_size', 'empty_image', 'invert_bit', 'or_bits']
print(all(x in dir(cil) for x in key_functions))
print(not any(x in dir(cil) for x in non_key_functions))