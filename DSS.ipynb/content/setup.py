{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMRoXXdAUJYwojheD4ifqq1"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "cm3y-VKOuvX3",
        "outputId": "587568c5-69d7-4a1f-887f-4802f6e072ce"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Writing mySort/mySort.py\n"
          ]
        }
      ],
      "source": [
        "%%writefile mySort/mySort.py\n",
        "\n",
        "\n",
        "\n",
        "# Bubble Sort\n",
        "def Bubble(A:list , N=None):\n",
        "    if N is None:\n",
        "        N = len(A)\n",
        "    \n",
        "    for i in range(N-1):\n",
        "        if A[i] > A[i+1]: A[i],A[i+1] = A[i+1],A[i]\n",
        "    if N > 1:\n",
        "        Bubble(A , N-1)\n",
        "    return A\n",
        "\n",
        "\n",
        "\n",
        "# Insertion Sort\n",
        "def Insertion(A:list , start=None, end=None):\n",
        "    if start is None and end is None:\n",
        "        start = 1\n",
        "        end = len(A)\n",
        "    \n",
        "    value = A[start]\n",
        "    loc = start \n",
        "    while loc > 0 and A[loc-1] > value:\n",
        "        A[loc] = A[loc-1]\n",
        "        loc -= 1\n",
        "    A[loc] = value \n",
        "    if start+1 < end:\n",
        "        Insertion(A , start+1 , end)\n",
        "    return A\n",
        "\n",
        "\n",
        "\n",
        "# Selection Sort\n",
        "def Selection(A:list , N=None):\n",
        "    if N is None:\n",
        "        N = len(A)\n",
        "    if N > 0:\n",
        "        SL = SLargest(A , N)\n",
        "        A[SL],A[N-1] = A[N-1],A[SL]\n",
        "        Selection(A , N-1)\n",
        "    return A\n",
        "\n",
        "def SLargest(A, last:int):\n",
        "    largest = 0\n",
        "    for i in range(last):\n",
        "        if A[i] > A[largest]: largest = i\n",
        "    return largest\n",
        "\n",
        "\n",
        "\n",
        "# Merge Sort\n",
        "def Merge(A:list , B=None , start=None , end=None):\n",
        "    if B is None and start is None and end is None:\n",
        "        B = [None]*len(A)\n",
        "        start = 0\n",
        "        end = len(A)-1\n",
        "    if start < end:\n",
        "        mid = (start + end)//2\n",
        "        Merge(A , B , start , mid)\n",
        "        Merge(A , B ,  mid+1 , end)\n",
        "        MergeCS(A , B , start , mid , end)\n",
        "    return A\n",
        "\n",
        "def MergeCS(A , B , start:int , mid:int , end:int):\n",
        "    front = start\n",
        "    back = mid+1\n",
        "    i = 0\n",
        "    while front <= mid and back <= end:\n",
        "        if A[front] <= A[back]:\n",
        "            B[i] = A[front]\n",
        "            i += 1\n",
        "            front += 1\n",
        "        else:\n",
        "            B[i] = A[back]\n",
        "            i += 1\n",
        "            back += 1\n",
        "    while front <= mid:\n",
        "        B[i] = A[front]\n",
        "        i += 1\n",
        "        front += 1\n",
        "    while back <= end:\n",
        "        B[i] = A[back]\n",
        "        i += 1\n",
        "        back += 1\n",
        "    for i in range(start, end+1):\n",
        "        A[i]=B[i-start]\n",
        "\n",
        "\n",
        "\n",
        "# Quick Sort\n",
        "def Quick(A:list , div=None , std=None):\n",
        "    if div is None and std is None:\n",
        "        div = 0\n",
        "        std = len(A)-1\n",
        "    if div < std:\n",
        "        mid = partition(A , div , std)\n",
        "        Quick(A , div , mid-1)\n",
        "        Quick(A , mid+1 , std)\n",
        "    return A\n",
        "\n",
        "def partition(A:list , div:int , std:int) -> int:\n",
        "    Stdvalue = A[std]\n",
        "    FEnd = div-1\n",
        "    for SStart in range(div,std):\n",
        "        if A[SStart] <= Stdvalue:\n",
        "            FEnd += 1\n",
        "            A[FEnd],A[SStart] = A[SStart],A[FEnd]\n",
        "    A[FEnd+1],A[std] = A[std],A[FEnd+1]\n",
        "    return FEnd+1\n",
        "\n",
        "\n",
        "\n",
        "# Heap Sort\n",
        "def Heap(A:list):\n",
        "    BuildHeap(A) \n",
        "    for last in range(len(A)-1,0,-1):\n",
        "        A[last], A[0] = A[0], A[last]\n",
        "        percolateDown(A,0,last-1)\n",
        "    return A\n",
        "\n",
        "def BuildHeap(A):\n",
        "    for i in range((len(A)-2) // 2, -1, -1): percolateDown(A , i , len(A)-1)\n",
        "\n",
        "def percolateDown(A , start:int , end:int):\n",
        "    left = 2*start+1\n",
        "    right = 2*start+2\n",
        "    if left <= end:\n",
        "        if right <= end and A[left] < A[right]: left = right\n",
        "        if A[start] < A[left]:\n",
        "            A[start], A[left] = A[left], A[start]\n",
        "            percolateDown(A, left, end)\n",
        "\n",
        "\n",
        "\n",
        "# Shell Sort\n",
        "def Shell(A:list):\n",
        "    G = GapSequence(len(A))\n",
        "    for gap in G:\n",
        "        for k in range(gap):\n",
        "            stepInsertion(A, k, gap)\n",
        "    return A\n",
        "\n",
        "def stepInsertion(A , k:int , gap:int):\n",
        "    for i in range(k + gap , len(A), gap):\n",
        "        j = i - gap\n",
        "        newItem = A[i]\n",
        "        while 0 <= j and newItem < A[j]:\n",
        "            A[j+gap] = A[j]\n",
        "            j -= gap\n",
        "        A[j+gap] = newItem\n",
        "\n",
        "def GapSequence(n:int) -> list:\n",
        "    G = [1]\n",
        "    gap = 1\n",
        "    while gap < n/5:\n",
        "        gap = 3*gap + 1\n",
        "        G.append(gap)\n",
        "    G.reverse()\n",
        "    return G\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "%%writefile setup.py\n",
        "\n",
        "import setuptools\n",
        "\n",
        "setuptool.setup(\n",
        "    name = 'MyDataSort001',\n",
        "    # 프로젝트 명을 입력합니다.\n",
        "    version = '0.0.1',\n",
        "    # 프로젝트 버전을 입력합니다.\n",
        "    url = \"https://github.com/YGC20\",\n",
        "    # 홈페이지 주소를 입력합니다.\n",
        "    download_url = \"https://github.com/YGC20\",\n",
        "    author = 'YGC20',\n",
        "    # 프로젝트 담당자 혹은 작성자를 입력합니다.\n",
        "    description = 'This is pip, which is a collection of functions used for data structures.',\n",
        "    # 프로젝트에 대한 간단한 설명을 입력합니다.\n",
        "    packages = ['mySort'],\n",
        "    # 기본 프로젝트 폴더 외에 추가로 입력할 폴더를 입력합니다.\n",
        "    classifiers=[\n",
        "        \"Programming Language :: Python :: 3\",\n",
        "        \"License :: OSI Approved :: MIT License\"\n",
        "    ]\n",
        ")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "NRc8quvqxPx1",
        "outputId": "2f7ba842-9b50-46c0-844f-cd3941215adf"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Writing setup.py\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install wheel"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "TNLP1NDQygSO",
        "outputId": "a69c95ee-8cf0-4d5a-cd0d-dad7d71c2a56"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/\n",
            "Requirement already satisfied: wheel in /usr/local/lib/python3.10/dist-packages (0.40.0)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install twine"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "pZhuwoV4yoNk",
        "outputId": "f0860f30-af9b-4d23-f96b-e491fe2e9dde"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/\n",
            "Collecting twine\n",
            "  Downloading twine-4.0.2-py3-none-any.whl (36 kB)\n",
            "Collecting pkginfo>=1.8.1 (from twine)\n",
            "  Downloading pkginfo-1.9.6-py3-none-any.whl (30 kB)\n",
            "Collecting readme-renderer>=35.0 (from twine)\n",
            "  Downloading readme_renderer-37.3-py3-none-any.whl (14 kB)\n",
            "Requirement already satisfied: requests>=2.20 in /usr/local/lib/python3.10/dist-packages (from twine) (2.27.1)\n",
            "Collecting requests-toolbelt!=0.9.0,>=0.8.0 (from twine)\n",
            "  Downloading requests_toolbelt-1.0.0-py2.py3-none-any.whl (54 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m54.5/54.5 kB\u001b[0m \u001b[31m7.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: urllib3>=1.26.0 in /usr/local/lib/python3.10/dist-packages (from twine) (1.26.15)\n",
            "Collecting importlib-metadata>=3.6 (from twine)\n",
            "  Downloading importlib_metadata-6.6.0-py3-none-any.whl (22 kB)\n",
            "Collecting keyring>=15.1 (from twine)\n",
            "  Downloading keyring-23.13.1-py3-none-any.whl (37 kB)\n",
            "Collecting rfc3986>=1.4.0 (from twine)\n",
            "  Downloading rfc3986-2.0.0-py2.py3-none-any.whl (31 kB)\n",
            "Requirement already satisfied: rich>=12.0.0 in /usr/local/lib/python3.10/dist-packages (from twine) (13.3.4)\n",
            "Requirement already satisfied: zipp>=0.5 in /usr/local/lib/python3.10/dist-packages (from importlib-metadata>=3.6->twine) (3.15.0)\n",
            "Collecting jaraco.classes (from keyring>=15.1->twine)\n",
            "  Downloading jaraco.classes-3.2.3-py3-none-any.whl (6.0 kB)\n",
            "Collecting SecretStorage>=3.2 (from keyring>=15.1->twine)\n",
            "  Downloading SecretStorage-3.3.3-py3-none-any.whl (15 kB)\n",
            "Collecting jeepney>=0.4.2 (from keyring>=15.1->twine)\n",
            "  Downloading jeepney-0.8.0-py3-none-any.whl (48 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m48.4/48.4 kB\u001b[0m \u001b[31m6.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: bleach>=2.1.0 in /usr/local/lib/python3.10/dist-packages (from readme-renderer>=35.0->twine) (6.0.0)\n",
            "Requirement already satisfied: docutils>=0.13.1 in /usr/local/lib/python3.10/dist-packages (from readme-renderer>=35.0->twine) (0.16)\n",
            "Requirement already satisfied: Pygments>=2.5.1 in /usr/local/lib/python3.10/dist-packages (from readme-renderer>=35.0->twine) (2.14.0)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests>=2.20->twine) (2022.12.7)\n",
            "Requirement already satisfied: charset-normalizer~=2.0.0 in /usr/local/lib/python3.10/dist-packages (from requests>=2.20->twine) (2.0.12)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests>=2.20->twine) (3.4)\n",
            "Requirement already satisfied: markdown-it-py<3.0.0,>=2.2.0 in /usr/local/lib/python3.10/dist-packages (from rich>=12.0.0->twine) (2.2.0)\n",
            "Requirement already satisfied: six>=1.9.0 in /usr/local/lib/python3.10/dist-packages (from bleach>=2.1.0->readme-renderer>=35.0->twine) (1.16.0)\n",
            "Requirement already satisfied: webencodings in /usr/local/lib/python3.10/dist-packages (from bleach>=2.1.0->readme-renderer>=35.0->twine) (0.5.1)\n",
            "Requirement already satisfied: mdurl~=0.1 in /usr/local/lib/python3.10/dist-packages (from markdown-it-py<3.0.0,>=2.2.0->rich>=12.0.0->twine) (0.1.2)\n",
            "Requirement already satisfied: cryptography>=2.0 in /usr/local/lib/python3.10/dist-packages (from SecretStorage>=3.2->keyring>=15.1->twine) (40.0.2)\n",
            "Requirement already satisfied: more-itertools in /usr/local/lib/python3.10/dist-packages (from jaraco.classes->keyring>=15.1->twine) (9.1.0)\n",
            "Requirement already satisfied: cffi>=1.12 in /usr/local/lib/python3.10/dist-packages (from cryptography>=2.0->SecretStorage>=3.2->keyring>=15.1->twine) (1.15.1)\n",
            "Requirement already satisfied: pycparser in /usr/local/lib/python3.10/dist-packages (from cffi>=1.12->cryptography>=2.0->SecretStorage>=3.2->keyring>=15.1->twine) (2.21)\n",
            "Installing collected packages: rfc3986, pkginfo, jeepney, jaraco.classes, importlib-metadata, requests-toolbelt, readme-renderer, SecretStorage, keyring, twine\n",
            "Successfully installed SecretStorage-3.3.3 importlib-metadata-6.6.0 jaraco.classes-3.2.3 jeepney-0.8.0 keyring-23.13.1 pkginfo-1.9.6 readme-renderer-37.3 requests-toolbelt-1.0.0 rfc3986-2.0.0 twine-4.0.2\n"
          ]
        }
      ]
    }
  ]
}