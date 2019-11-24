import json

output_list = []
#STATE = 'preprocessing'
STATE = 'generate'

if STATE == 'preprocessing' :
    ## preprocessing file
    fp = open('input.txt', "r")
    line = fp.readline()
    
    output_char = []
    i = 0 
    while line:
        if i % 2 == 0 :
            _ = "" 
            for idx, i_char in enumerate(line) :
                if i_char != '~' and i_char != '！' and i_char != '，' :
                    _ += i_char
                else :
                    _ += '-'
                if idx != len(line)-1 :
                    _ += ' '
            output_char.append(_)
        line = fp.readline()
        i += 1

    file_temp = open("output_temp.txt","w")  
    file_temp.writelines(output_char) 
    file_temp.close() 
elif STATE == 'generate':
    fp1 = open('input.txt', "r")
    fp2 = open('input_2.txt', "r")

    line_1 = fp1.readline()
    line_2 = fp2.readline()

    i = 0 
    url_list = []
    content_list = []

    while line_1:
        if i % 2 == 0 :
            line_1 = line_1.replace(" ", "").rstrip()
            print(line_1)
            _ = ""
            line_2 = line_2.split()
            for idx, i_char in enumerate(line_1) :
                if i_char != '~' and i_char != '！' and i_char != '，' :
                    write_char = '<ruby>'+i_char+'<rt>'+line_2[idx]+'</rt></ruby>'
                else :
                    write_char = i_char
                _ += write_char
            content_list.append(_)  
            line_2 = fp2.readline()
        else :
            url = (line_1[0:24] + 'embed/' + line_1[32:]).rstrip()
            if len(url.split('#')) == 2 :
                url = url.split('#')
                time = url[1].split('=')[1].split('m') 
                if len(time) == 2 :
                    time = int(time[0]) * 60 + int(time[1].split('s')[0] )
                else :
                    time = int(time[0].split('s')[0] )
                url = url[0] + '?start=' + str(time) + '&autoplay=1'
            url_list.append(url)

        line_1 = fp1.readline()
        i += 1

    output_char = []
    for i in range(0, 6) :
        temp_dic = { 'url': [], 'content' : [] }
        for j in range(0, 6) :
            temp_dic['url'].append(url_list[i*6+j])
            temp_dic['content'].append(content_list[i*6+j])
        output_char.append(temp_dic)

with open('content.json', 'w') as f:
    json.dump(output_char, f)
with open('content.json') as json_file:
    data = json.load(json_file)
print(data)