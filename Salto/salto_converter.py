import re


def salto_converter_from_number(salto_number_string):
    salto_number = int(salto_number_string)
    salto_number = hex(salto_number)
    hex_array = []
    for i in range(2, len(salto_number), 2):
        hex_array.append(salto_number[i:i + 2])
    hex_array.reverse()
    block1 = hex_array[0:2]
    block2 = hex_array[2:4]
    block1 = ''.join(block1)
    block2 = ''.join(block2)
    block1 = int(block1, 16)
    block2 = int(block2, 16)
    combined = str(block1) + str(block2)
    combined = combined[1:]
    return combined


def salto_converter_from_hex(salto_hex):
    n = 2
    hex_array = [salto_hex[i:i + n] for i in range(0, len(salto_hex), n)]
    hex_array.reverse()
    block1 = hex_array[0:2]
    block2 = hex_array[2:4]
    block1 = ''.join(block1)
    block2 = ''.join(block2)
    block1 = str(int(block1, 16))
    block2 = str(int(block2, 16))
    while len(block1) < 5:
        block1 = '0'+block1
    while len(block2) < 5:
        block2 = '0'+block2
    combined = str(block1) + str(block2)
    combined = combined[1:]
    return combined


"""
old_test_code = '0342410963'
print salto_converter_from_number(old_test_code)
salto_code1 = '049BC6D3000000'
salto_code2 = 'D4D3C6D3000000'
salto_list = [salto_code1, salto_code2]
"""

"""
with open('/Users/Kristian/Google Drive/Developer/Small-projects/Salto/josteins_koder.txt') as f:
    content = f.readlines()

print content
content = map(lambda l: l.split(' '), content)
print content
for line in content:
    line = line[-1]
    print salto_converter_from_hex(line[0:8])
# for salto_code in:
#     print salto_converter_from_hex(salto_code[0:8])
"""

with open('/Users/Kristian/Google Drive/Developer/Small-projects/Salto/josteins_koder.txt') as f:
    content = f.readlines()

for line in content:
    print salto_converter_from_hex(line.strip()[0:8])
# salto_test = "8414C7D3000000"
# salto_converter_from_hex(salto_test[0:8])


"""
public static String toVisionMyfairRCO(String saltoNumber) {
        //String saltohex = Long.toHexString(Long.parseLong(saltoNumber));
        String saltohex = saltoNumber;
        saltohex = saltohex.replaceAll("(.{2})(?!$)", "$1 ").trim();
        String[] hexArray = saltohex.split(" ");
        ArrayList<String> hexList = new ArrayList(Arrays.asList(hexArray));
        Collections.reverse(hexList);
        String block1 = hexList.get(0) + hexList.get(1);
        String block2 = hexList.get(2) + hexList.get(3);
        block1 = Integer.toString(Integer.parseInt(block1, 16));
        block2 = Integer.toString(Integer.parseInt(block2, 16));
        return block1.substring(1).concat(block2);
    }

    public static String toRCO(String saltoNumber){
        //String saltohex = Long.toHexString(Long.parseLong(saltoNumber));
        String saltohex = saltoNumber;
        saltohex = saltohex.replaceAll("(.{2})(?!$)", "$1 ").trim();
        String[] hexArray = saltohex.split(" ");
        ArrayList<String> hexList = new ArrayList(Arrays.asList(hexArray));
        Collections.reverse(hexList);
        saltohex = hexList.get(0)+hexList.get(1)+hexList.get(2)+hexList.get(3);
        return Long.toString(Long.parseLong(saltohex, 16)).substring(1);
    }

    public static void main(String[] args) {
        System.out.println(toVisionMyfairRCO("0342410963"));
        System.out.println(toRCO("0342410963"));

        String desktop = System.getProperty("user.home") + "/Desktop";
        System.out.println(desktop);
        System.out.println(System.getProperty("os.name"));
        String number = "1468C6D3000000";
        System.out.println(number.substring(0, number.length() - 6));



        //Long a = Long.parseLong("d3c66814",16);
        //System.out.println(a.toString().substring(1));
    }
"""
