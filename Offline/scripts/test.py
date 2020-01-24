#from ecdsa import SigningKey,NIST384p
# from fastecdsa import curve, ecdsa, keys
#from comm.functions import *
import qrcode
#import base64
#from Crypto.PublicKey import RSA
#from Crypto import Random
#from Crypto.Hash import SHA256
#from Crypto.Signature import PKCS1_v1_5
import subprocess
#import PyPDF2
import base64

# # creating a pdf file object
# pdfFileObj = open('/home/bcsadmin/Downloads/form3.pdf', 'rb')
#
# # creating a pdf reader object
# pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
#
# # printing number of pages in pdf file
# print(pdfReader.numPages)
#
# # creating a page object
# pageObj = pdfReader.getPage(0)
#
# # extracting text from page
# print(pageObj.extractText())
#
# # closing the pdf file object
# pdfFileObj.close()



# def digital_ecryption():
#     try:
#         data = '{"Data": {"Name": "Sunil", "Mobile": 7276195142, "Address": "Warje,Pune 411058"}}'
#         # data1 = '{"Data": {"Name": "Sunil", "Mobile": 7276195142, "Address": "Warje,Pune 411058"}}'
#
#         if type(data) is str:
#             data = bytes(data, encoding='utf-8')
#
#         KEYSIZE = 256 * 8
#         random_generator = Random.new().read
#         RSAkey = RSA.generate(KEYSIZE,
#                               randfunc=random_generator,
#                               progress_func=None)
#                               # e=65537)
#
#         public_key = RSAkey.publickey()
#
#         enc_data = public_key.encrypt(data, 32)
#
#         dec_date = RSAkey.decrypt(enc_data)
#
#         # sk = SigningKey.generate(curve=NIST384p)  # uses NIST192p
#         # vk = sk.get_verifying_key()
#         # # sk_string = sk.to_string()
#         # # vk_string = vk.to_string()
#         # signature = sk.sign(enc_data[0])
#         # try:
#         #     vk.verify(signature, enc_data[0])
#         #     print("Signature verified.")
#         # except:
#         #     print("Bad Signature.")
#
#
#         # hash = SHA256.new(data).digest()
#
#         signature = RSAkey.sign(enc_data[0],'')
#
#         verify = public_key.verify(signature,enc_data[0])
#
#         print(verify)
#
#     except Exception as e:
#         raise e
#
# def encryption():
#     try:
#         result = b'{"Data":{"Name":"Sunil","Mobile":7276195142,"Address":"Warje,Pune 411058"}}'
#         sk = SigningKey.generate(curve=NIST384p) # uses NIST192p
#         vk = sk.get_verifying_key()
#         sk_string = sk.to_string()
#         vk_string = vk.to_string()
#         print(vk_string)
#         print(sk_string)
#         # a = sk.to_pem()
#         print(sk)
#         print(vk)
#         # a = vk.encrypt(result, 32)
#         # print(a)
#         # vk.encrypt(result)
#         signature = sk.sign(result)
#
#
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=2,
)
qr.add_data(7276195142)
qr.make(fit=True)
img = qr.make_image()
img.save('QR.jpg','JPEG')
#
#         try:
#             vk.verify(signature, result)
#             print("Signature verified.")
#         except:
#             print("Bad Signature.")
#     except Exception as e:
#         raise e
# try:
#      # Variable number of args in a list
#         args = '/home/bcsadmin/Downloads/IMG-9016.JPG'
#         # Build subprocess command
#         cmd = 'Rscript /home/bcsadmin/upruf/scripts/LicenceNum.R '+args
#         a = subprocess.check_output(cmd,shell=True)
#         a = a.decode('UTF-8')
#         print(a)
#
# #     a = a.decode('UTF-8')
# #     a = a.split(" ")[1].rstrip("\n").strip('"')
# #     print(a)
# except Exception as e:
#     raise e

from sanic import Sanic
from sanic.response import file
from sanic.views import CompositionView
from sanic.views import HTTPMethodView
from sanic.views import stream as stream_decorator
from sanic.blueprints import Blueprint
from sanic.response import stream, text,json
import time
app = Sanic('request_stream')
# @app.route('/')
# async def index(request):
#     return await file('demo.html')
#
#
# @app.websocket('/feed')
# async def feed(request, ws):
#     i = 0
#     while True:
#         await ws.recv()
#         i = i+1
#         await ws.send("Completed"+str(i))

# import pyqrcode
# url = pyqrcode.create('sunil')
# url.svg('sunil.svg', scale=8)
# print(url.terminal(quiet_zone=1))


# encodeString = encodeString(
#                             encodestr="username=" + addorg.get('hrEmail') + "&role=CHR" + "&IsRegister=0")verify@unipruf.com
# encoded = "username=verify@uberpruf.com&role=VAD&IsRegister=0".encode('ascii')
# encoded = base64.b64encode(encoded)
# encoded = str(encoded).rstrip("'")
# encoded = str(encoded).lstrip("b'")
# encoded = str(encoded).rstrip('==')
# encoded1 = "https://app.uberpruf.com/reset-password/"+encoded
# #encoded2 = "https://app.unipruf.com/reset-password/"+encoded
# print(encoded)

# bp = Blueprint('blueprint_request_stream')
#
#
# class SimpleView(HTTPMethodView):
#
#     @stream_decorator
#     async def post(self, request):
#         result = 1
#         while True:
#             body = await request.stream.get()
#             if body is None:
#                 break
#             result += 1
#         return text("asd"+str(result))
#
#
# @app.post('/stream', stream=True)
# async def handler(request):
#     async def streaming(response):
#         while True:
#             body = await request.stream.get()
#             if body is None:
#                 break
#             # body = body.decode('utf-8')
#             body = str(body)
#             response.write(body)
#     return stream(streaming)
#
#
# @bp.put('/bp_stream', stream=True)
# async def bp_handler(request):
#     result = ''
#     while True:
#         body = await request.stream.get()
#         if body is None:
#             break
#         result += body.decode('utf-8').replace('1', 'A')
#     return text(result)
#
#
# async def post_handler(request):
#     try:
#         result = 1
#         while True:
#             # filename = "a.jpeg"
#             body = await request.stream.get()
#
#             if body is None:
#                 break
#             result += 1
#         time.sleep(70)
#         return json(str(result))
#         # current_date = datetime.utcnow().strftime('%Y%m%d_%H%M%S')
#         # filename = filename.split(".")
#         # fil_nm = filename[0] + "_" + current_date
#         # filename = fil_nm + "." + filename[1]
#         # data = base64.b64encode(result[0])
#         # # image_64_encode = base64.encodestring(result[0])
#         # image_64_decode = base64.decodestring(data)
#         # image_result = open(filename,
#         #                     'wb')
#         # image_result.write(image_64_decode)
#
#         # return text("g")
#     except Exception as e:
#         raise e
# app.blueprint(bp)
# app.add_route(SimpleView.as_view(), '/method_view')
# view = CompositionView()
# view.add(['POST'], post_handler, stream=True)
# app.add_route(view, '/composition_view')
# @app.route("/test")
# async def test_large_dynamic_file(request):
#     async def stream_file(resp):
#         nonlocal _file
#         read_file = functools.partial(_file.read, 8192)
#         finished_read = asyncio.Event(loop=loop)
#         finished_write = asyncio.Event(loop=loop)
#         latest_chunk = b''
#
#         async def read_fn():
#             nonlocal latest_chunk
#             latest_chunk = await read_file()
#             loop.call_soon(finished_read.set)
#
#         async def write_fn():
#             resp.write(latest_chunk)
#             loop.call_soon(finished_write.set)
#
#         try:
#             while True:
#                 finished_read.clear()
#                 scheduled_read_handle = loop.call_soon(lambda: asyncio.ensure_future(read_fn(), loop=loop))
#                 _ = await finished_read.wait()
#                 if len(latest_chunk) < 1:
#                     break
#                 finished_write.clear()
#                 scheduled_write_handle = loop.call_soon(lambda: asyncio.ensure_future(write_fn(), loop=loop))
#                 _ = await finished_write.wait()
#         except Exception as e:
#             print(e)
#         finally:
#             await _file.close()
#         return  # returning from this fn closes the stream
#
#     return StreamingHTTPResponse(stream_file, status=200)


# from model.key import get_hashed_pass, get_key
# PassHash, PassPhraseSalt = get_hashed_pass(password="Anubhav@01")
# print(PassHash)
# print(PassPhraseSalt)
# for convert html to pdf
# import pdfkit
# pdfkit.from_file('/home/bcsadmin/Desktop/index.html','pdf.pdf')
# with open(PDF_PATH + username + '.pdf', "rb") as pdf_file:
#     data = pdf_file.read()

if __name__ == '__main__':
    app.run(host='192.168.10.108', port=9090,workers=2)
# #

# if __name__ == "__main__":
#     print("started")
#     #print(datetime.datetime.now())
#     # encryption()
#     digital_ecryption()
#     print("end")
#     #print(datetime.datetime.now())