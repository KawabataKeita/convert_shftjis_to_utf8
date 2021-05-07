import os
import codecs
import io

def convert_shiftjis_to_utf8(shiftjis_path,utf8_path):
    #shift_jis_folder_pathの直下に新たにフォルダを作成するさいに指定：（例）'new/'
    #shift_jis_folder_pathの直下で作成する場合は''にする
    new_folder = ''
    for curDir, dirs, files in os.walk(shiftjis_path):
        for file in files:
            if '.DS_Store' == file:
                continue
            existed_folder = curDir.split('/')[-1]
            folder = utf8_path+'/'+ new_folder
            os.makedirs(folder +existed_folder, exist_ok=True)
            #print(utf8_path+'/'+ new_folder +folder)
            shift_jis_file_path = curDir + '/' + file 
            shift_jis_text = codecs.open(shift_jis_file_path, "r", "shift_jis",'ignore')
            utf_8_text = codecs.open(folder +existed_folder+ '/'+file, "w", "utf-8")
            for row in shift_jis_text:
                utf_8_text.write(row)
            shift_jis_text.close()
            utf_8_text.close()


#shift_jisファイルがあるフォルダのパス
shift_jis_folder_path = ''
#utf8に変換したファイルを置くディレクトリ
utf_8_folder_path = ''

convert_shiftjis_to_utf8(shift_jis_folder_path,utf_8_folder_path)
print('finish')
