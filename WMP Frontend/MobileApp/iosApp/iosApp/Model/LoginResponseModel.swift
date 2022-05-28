//
//  LoginResponseModel.swift
//  iosApp
//
//  Created by Daniel Ghebrat on 22/05/2022.
//

import Foundation
// This file was generated from JSON Schema using quicktype, do not modify it directly.
// To parse the JSON, add this file to your project and do:
//
//   let welcome = try? newJSONDecoder().decode(Welcome.self, from: jsonData)

// MARK: - WelcomeElement
struct LoginResponseModel: Codable {
    let username: String?
    let userAttributes: [UserAttribute]?
    let responseMetadata: ResponseMetadata?
    let accessToken: String?

    enum CodingKeys: String, CodingKey {
        case username = "Username"
        case userAttributes = "UserAttributes"
        case responseMetadata = "ResponseMetadata"
        case accessToken
    }
}

// MARK: - ResponseMetadata
struct ResponseMetadata: Codable {
    let requestID: String
    let httpStatusCode: Int
    let httpHeaders: HTTPHeaders
    let retryAttempts: Int

    enum CodingKeys: String, CodingKey {
        case requestID = "RequestId"
        case httpStatusCode = "HTTPStatusCode"
        case httpHeaders = "HTTPHeaders"
        case retryAttempts = "RetryAttempts"
    }
}

// MARK: - HTTPHeaders
struct HTTPHeaders: Codable {
    let date, contentType, contentLength, connection: String
    let xAmznRequestid: String

    enum CodingKeys: String, CodingKey {
        case date
        case contentType = "content-type"
        case contentLength = "content-length"
        case connection
        case xAmznRequestid = "x-amzn-requestid"
    }
}

// MARK: - UserAttribute
struct UserAttribute: Codable {
    let name, value: String

    enum CodingKeys: String, CodingKey {
        case name = "Name"
        case value = "Value"
    }
}


import Foundation

// MARK: - Welcome
struct FailedAuth: Codable {
    let detail: String
}


typealias LoginModel = [LoginResponseModel]
