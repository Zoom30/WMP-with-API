package com.example.mobileapp

class Greeting {
    fun greeting(): String {
        return "Hello, ${Platform().platform}!"
    }
}