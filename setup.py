import setuptools

setuptool.setup(
    name = 'MyDataSort001',
    # 프로젝트 명을 입력합니다.
    version = '0.0.1',
    # 프로젝트 버전을 입력합니다.
    url = "https://github.com/YGC20",
    # 홈페이지 주소를 입력합니다.
    download_url = "https://github.com/YGC20",
    author = 'YGC20',
    # 프로젝트 담당자 혹은 작성자를 입력합니다.
    description = 'This is pip, which is a collection of functions used for data structures.',
    # 프로젝트에 대한 간단한 설명을 입력합니다.
    packages = ['mySort'],
    # 기본 프로젝트 폴더 외에 추가로 입력할 폴더를 입력합니다.
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ]
)
