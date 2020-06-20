# 파일 읽어오기
with open("vane_requirement.txt", 'r') as vane_file:
    vane_pkg = vane_file.read()
      
with open("pinwheel_requirement.txt", 'r') as pinwheel_file:
    pinwheel_pkg = pinwheel_file.read()
  
# vane 패키지 설치내역 리스트로 만들기(버전 정보 포함)
vane_list = [_.split()[0] for _ in vane_pkg.split("\n") if _ is not ""]

# pinwheel 패키지 설치내역 리스트로 만들기 (버전 정보 제외)
pinwheel_list = [_.split()[0] for _ in pinwheel_pkg.split("\n") if _ is not ""]
pinwheel_list = [_.split("==")[0] for _ in pinwheel_list]

# 설치되지 않은 패키지 찾기
requirement = []
for _ in vane_list:
    if _.split("==")[0] not in pinwheel_list:
        requirement.append(_)

# requirement.txt 저장하기
with open("requirement.txt", "w") as f:
    for _ in requirement:
        f.writelines(_ + "\n")
