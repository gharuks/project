import { Component, OnInit } from '@angular/core';
import {NgForm} from '@angular/forms';


@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.css']
})
export class SignupComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
  }

  // tslint:disable-next-line:typedef
  onFormSubmit(userForm: NgForm) {
    console.log(userForm.value);
    console.log('Name:' + userForm.controls.name.value);
    console.log('Form Valid:' + userForm.valid);
    console.log('Form Submitted:' + userForm.submitted);
  }
  // tslint:disable-next-line:typedef
  resetUserForm(userForm: NgForm) {
    userForm.resetForm();
  }

}