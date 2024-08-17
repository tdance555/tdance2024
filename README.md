# 關於本程式

## 安裝

本專案程式係採用 Django 框架開發，所以欲參與此專案的人員，應先準備好 python 的執行環境，
同時需要安裝 pipenv 套件，最後可以利用 Pipfile 的檔案安裝相依的套件。

## 程式架構

本專案的根目錄是 `tdance2024`，裡面有兩個子專案，分別取名為 `mysite` 及 `trips`，其
中 `trips` 是本次專案主要程式範圍，用來設計要跟 WebAR 遊戲程式串接的功能。

在此架構下，本專案會需要建置資料庫及相應的資料表，其資料結構請參考 `trips/models.py`
檔案，而資料庫檔案在 `db.sqlite3`。由於資料庫檔案儲存了真正需要使用的資料，因此一旦有使
用這個專案新增任何資料（例如參與單位的介紹、問題與答案等），都需要再將 `db.sqlite3` 更
新至這個儲存庫（repository）。

## Git 更新程式的流程

1. （在 VSCode）修改程式碼
2. 儲存檔案
3. 回到終端機
4. 下 `git status` 確認這次的變更範圍
5. 使用 `git add [file]` 將變更的檔案加入你此次的 commit 追蹤範圍（或是可以直接下
   `git add .` 代表將所有有變更的檔案都加入
6. 接著就是使用 `git commit` 將此次的範圍記錄變成 git log，也就是實際建立一個變更點
   （通常可以用 `git commit -m "此次變更的簡要記錄"` 指令）
7. 最後就是下 `git push` 真正將變更發佈到 github，發佈之後，其他專案的成員才能透過
   `git pull` 來取得最新的程式內容

## APIs

### 建立使用者

如果要建立使用者，只要利用 `POST` 方法朝以下 API 傳送包含 `phone` 及 `gender` 的資訊，即可建立一組使用者帳號。

```
POST /trips/api/user/
BODY
{
   "phone": "0000000000",
   "gender": "M"
}
```

### 取得使用者過關歷程

如果要取得使用者的過關歷程，可以利用 `GET` 方法一樣呼叫 `/trips/api/user/` API，使用方法如下。

```
GET /trips/api/user/?phone=0000000000&level=1

parameters
- phone（必填）: 使用者的行動電號，10 碼
- level（選填）: 關卡代號
```

範例
1. 取得使用者及所有過關資料
`GET http://127.0.0.1:8000/trips/api/user/?phone=0918697537`
回傳結果
```
{
    "phone": "0918697537",
    "gender": "M",
    "post": {
        "content": {
            "1": {
                "status": "null",
                "user_answer": "",
                "correct_answer": ""
            },
            "2": {
                "status": "null",
                "user_answer": "",
                "correct_answer": ""
            },
            "3": {
                "status": "null",
                "user_answer": "",
                "correct_answer": ""
            },
            "4": {
                "status": "null",
                "user_answer": "",
                "correct_answer": ""
            },
            "5": {
                "status": "null",
                "user_answer": "",
                "correct_answer": ""
            },
            "6": {
                "status": "null",
                "user_answer": "",
                "correct_answer": ""
            },
            "7": {
                "status": "null",
                "user_answer": "",
                "correct_answer": ""
            },
            "8": {
                "status": "null",
                "user_answer": "",
                "correct_answer": ""
            },
            "9": {
                "status": "null",
                "user_answer": "",
                "correct_answer": ""
            },
            "10": {
                "status": "null",
                "user_answer": "",
                "correct_answer": ""
            },
            "11": {
                "status": "null",
                "user_answer": "",
                "correct_answer": ""
            },
            "12": {
                "status": "null",
                "user_answer": "",
                "correct_answer": ""
            },
            "13": {
                "status": "null",
                "user_answer": "",
                "correct_answer": ""
            },
            "14": {
                "status": "null",
                "user_answer": "",
                "correct_answer": ""
            },
            "15": {
                "status": "null",
                "user_answer": "",
                "correct_answer": ""
            },
            "16": {
                "status": "null",
                "user_answer": "",
                "correct_answer": ""
            },
            "17": {
                "status": "null",
                "user_answer": "",
                "correct_answer": ""
            },
            "18": {
                "status": "null",
                "user_answer": "",
                "correct_answer": ""
            },
            "19": {
                "status": "null",
                "user_answer": "",
                "correct_answer": ""
            },
            "20": {
                "status": "null",
                "user_answer": "",
                "correct_answer": ""
            },
            "21": {
                "status": "null",
                "user_answer": "",
                "correct_answer": ""
            },
            "22": {
                "status": "null",
                "user_answer": "",
                "correct_answer": ""
            },
            "23": {
                "status": "null",
                "user_answer": "",
                "correct_answer": ""
            },
            "24": {
                "status": "null",
                "user_answer": "",
                "correct_answer": ""
            },
            "25": {
                "status": "null",
                "user_answer": "",
                "correct_answer": ""
            },
            "26": {
                "status": "null",
                "user_answer": "",
                "correct_answer": ""
            },
            "27": {
                "status": "null",
                "user_answer": "",
                "correct_answer": ""
            },
            "28": {
                "status": "null",
                "user_answer": "",
                "correct_answer": ""
            },
            "29": {
                "status": "null",
                "user_answer": "",
                "correct_answer": ""
            }
        },
        "updated_at": "2024-08-17T05:41:00.104262Z"
    }
}
```

2. 只取得某使用者某個關卡的過關資料
`GET http://127.0.0.1:8000/trips/api/user/?phone=0918697537&level=1`
回傳結果
```
{
    "1": {
        "status": "null",
        "user_answer": "",
        "correct_answer": ""
    }
}
```

### 更新過關記錄

如果要更新使用者的過關記錄，可以利用以下 API，輸入要更新的關卡及過關資訊等。

```
PATCH /trips/api/post/<str:phone>/
BODY
{
    "level": "1",
    "status": "pass",
    "user_answer": "A",
    "correct_answer": "A"
}
```


## 常見問題

### 資料庫問題

如果在更新程式後，遇到資料庫問題，可以嘗試用刪除整個資料庫再重新建立。但要注意，資料庫刪除不能還原，所以在操作時務必小心。

```
$ rm db.sqlite3
$ python manage.py migrate
```

### 最高管理者帳號、密碼忘記

如果忘記最高管理者帳號或密碼，而無法登入 `admin` 後台的話，可以利用以下指令重設最高管理者帳號、密碼。

```
$ python manage.py createsuperuser
```