# -*- coding: utf-8 -*-
import requests, re, time, os, math

headers = {'Host': 'www.icourse163.org',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
'Accept-Encoding': 'gzip, deflate',
'Content-Type': 'text/plain',
'Connection': 'keep-alive'}


dataGetMocTermDto = {'callCount':'1',
'scriptSessionId':'${scriptSessionId}190',
'c0-scriptName':'CourseBean',
'c0-methodName':'getMocTermDto',
'c0-id':'0',
'c0-param0':'number:1001962001',                        #tid 课程学期Id
'c0-param1':'number:1',
'c0-param2':'boolean:true',
'batchId':'1490456943066'}

def getHTMLText(url, data):
    try:
        res = requests.post(url, headers = headers, data = data)
        res.raise_for_status()
        return res.text
    except:
        print('[-]ERROR: post error')

if __name__ == '__main__':
    getMocTermDtoUrl = 'http://www.icourse163.org/dwr/call/plaincall/CourseBean.getMocTermDto.dwr'
    # url = 'http://www.icourse163.org/dwr/call/plaincall/CourseBean.getMocTermDto.dwr'

    resText = getHTMLText(getMocTermDtoUrl, dataGetMocTermDto)
    content = resText.encode('utf-8').decode('unicode_escape')

    re_getPdf = r'http://nos.netease.com/.*?\.pdf'
    pdfUrl = re.search(re_getPdf, content)
    # pdf = requests.get(pdfUrl)
    # with open('{}/{}.pdf'.format(path, pdfName), 'wb') as file:
    #     file.write(pdf.content)
# pdfUrl = parsePageInfo(resText)
# pdf = requests.get(pdfUrl)
# with open('{}/{}.pdf'.format(path, pdfName), 'wb') as file:
#     file.write(pdf.content)
#     print(content)
#     names = [name[1] for name in re.findall(u's(\d+).name=(.*?);', content)]
    # for i, name in enumerate(names):
    #     print([i, name])
    # print(content)
    print(pdfUrl)
    # for name in names:
    #     print(name)
# print(u'"\u3010\u7b2c\u3007\u5468\u3011\u7f51\u7edc\u722c\u866b\u4e4b\u524d\u594f"')