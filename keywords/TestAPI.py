#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests


class TestAPI(object):
    def __init__(self):
        self.url = ''
        self.service_url = ''
        self.request_data = ''
        self.expected_status_code = ''
        self.expected_response_content = ''
        self.test_data = {}

    def init_test_env(self, url: str):
        self.url = url

    def load_test_data(self, status_code, response_content: str):
        self.test_data = {
            u'期望状态码': int(status_code),
            u'期望返回值': response_content,
        }

    def request_validation(self, method: str, path: str):
        expected_status_code = self.test_data[u'期望状态码']
        expected_response_content = self.test_data[u'期望返回值']
        if method == 'GET':
            response = requests.get(url=self.url + path)
        elif method == 'POST':
            response = requests.post(url=self.url + path)
        else:
            assert False, u'方法错误'
        assert response.status_code == expected_status_code, \
            u'状态码不符合预期: 预期=%s 实际=%s' % (expected_status_code, response.status_code)
        print(u'状态码符合预期: %s' % response.status_code)
        assert expected_response_content in str(response.content.decode('utf-8')), \
            u'返回值不符合预期: 预期=%s 实际=%s' % (expected_response_content, response.content.decode('utf-8'))
        print(u'返回值符合预期: %s' % response.content.decode('utf-8'))
        response.close()


if __name__ == '__main__':
    print('This is Keywords script for Miracle demo')

