//
//  ViewController.swift
//  iosApp
//
//  Created by Daniel Ghebrat on 20/05/2022.
//

import UIKit
import shared

class ViewController: UIViewController {
    
    let apiAccess = APIHandler()
    
    @IBOutlet weak var emailTextField: UITextField!
    @IBOutlet weak var passwordTextField: UITextField!
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        hideKeyboardWhenTappedAround()
        resizeViewOnKeyboardAppearDisappear()
        
        
    }
    
    @IBAction func signInPressed(_ sender: UIButton) {
        guard let email = emailTextField.text else {
            return
        }
        guard let password = passwordTextField.text else {
            return
        }
        apiAccess.signIn(email: email, password: password) { result, error in
            if let apiResponse = result {
                print(apiResponse.description())
            }
        }
        
        
    }
    

}
