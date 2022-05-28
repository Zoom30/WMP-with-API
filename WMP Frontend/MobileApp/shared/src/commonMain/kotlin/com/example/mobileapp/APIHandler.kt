package com.example.mobileapp

import io.ktor.client.*
import io.ktor.client.call.*
import io.ktor.client.request.*
import io.ktor.client.statement.*
import io.ktor.http.*
import io.ktor.util.*

class APIHandler {
    private val httpClient = HttpClient()
    val url: String = "http://localhost:8000"


    suspend fun checkHealth(): String {
        val response: HttpResponse = httpClient.get(url)
        return response.bodyAsText()
    }

    @OptIn(InternalAPI::class)
    suspend fun signIn(email: String, password: String): HttpResponse {
        val response: HttpResponse = httpClient.post("$url/sign_in?email=$email&password=$password")
        return response.body()
    }


}