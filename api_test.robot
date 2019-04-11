*** Settings ***
Documentation       Miracle Service API Testing
Library             keywords/TestAPI.py

*** Variables ***
${前段地址}         http://10.12.21.11:31080
${后端地址}         http://10.12.21.11:31880

*** Test Cases ***
TestCase-001 Health Check
    [Tags]    API
    初始化测试环境     ${后端地址}
    装载测试数据       预期状态码=200      预期返回值=success
    测试接口          方法=GET    接口=/health

TestCase-002 Error 404
    [Tags]    API
    初始化测试环境     ${后端地址}
    装载测试数据       预期状态码=404      预期返回值=Not Found
    测试接口          方法=GET    接口=/404

*** Keywords ***
初始化测试环境
    [Arguments]     ${url}
    INIT TEST ENV   ${url}

装载测试数据
    [Arguments]     ${预期状态码}        ${预期返回值}
    LOAD TEST DATA      status_code=${预期状态码}        response_content=${预期返回值}

测试接口
    [Arguments]     ${方法}     ${接口}
    REQUEST VALIDATION      method=${方法}     path=${接口}
