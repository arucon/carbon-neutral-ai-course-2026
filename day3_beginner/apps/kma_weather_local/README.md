# 기상청 초단기예보 로컬 웹앱

Notebook에서 확인한 기상청 초단기예보 응답을 Streamlit 화면으로 연결합니다. 자료는 실행 중 메모리에만 머물며, 사용자가 내려받기 버튼을 눌렀을 때 CSV 파일로 저장할 수 있습니다.

## 1. 터미널에서 앱 폴더로 이동

```bash
cd apps/kma_weather_local
```

## 2. 가상환경 만들기

macOS 또는 Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows PowerShell:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

## 3. 필요한 패키지 설치

```bash
python -m pip install -r requirements.txt
```

## 4. API 키 저장

`.env.example`을 `.env`라는 이름으로 복사하고, 등호 오른쪽에 준비한 키를 넣습니다.

```text
KMA_AUTH_KEY=
```

등호 오른쪽에 준비한 키를 붙여 넣습니다. 이 파일은 화면이나 Git 저장소에 올리지 않습니다. 키 값은 웹 화면에 표시되지 않습니다.

## 5. 앱 실행

```bash
python -m streamlit run app.py
```

브라우저가 자동으로 열리지 않으면 터미널에 표시된 `http://localhost:8501` 주소를 엽니다.

API 키가 아직 저장되지 않은 경우에는 함께 제공된 기상청 응답 형식 샘플로 화면과 CSV 저장 기능을 확인할 수 있습니다.

## 파일 구성

- `app.py`: 화면과 사용자 선택
- `kma_client.py`: API 요청, 응답 확인, 표 변환
- `.env`: 개인 API 키를 저장하는 로컬 파일
- `requirements.txt`: 앱 실행에 필요한 Python 패키지

API 문서: https://apihub.kma.go.kr/apiList.do?seqApi=10
