## Flask Rest API backend

### Setting up the environment

Navigate to cie_capstone_repo/new_backend and run the following code:
```
pip install -r requirement.txt
```
### Run the server

In the terminal, run:
```
python main.py
```
### Test the Post and Get request

* In **test.py**, there are pre-written json data to test on. If you want to use different data or different arrangement of the json data, make the changes to the variable **data** in **test.py**.
* **test.py** will automatically run the **POST** request to the server and use the response to run the **GET** request.
* **test.py** will then use the response from the **GET** request to open a new browser window which will navigate you to the QR Code which was generated using the data you passed in.

In a separate terminal, run:
```
python test.py
```
The browser should be opened and you should be able you view and scan your qr code.
