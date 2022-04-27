import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { FormBuilder, FormGroup, Validators , ReactiveFormsModule} from '@angular/forms';
import {UserService} from '../user.service';
import {User} from '../user';

@Component({
  selector: 'app-registration',
  templateUrl: './registration.component.html',
  styleUrls: ['./registration.component.css']
})
export class RegistrationComponent implements OnInit {
  registerForm: FormGroup = this.formBuilder.group({
    // firstName: ['', Validators.required],
    //   lastName: ['', Validators.required],
      username: ['', Validators.required],
      password: ['', [Validators.required, Validators.minLength(5)]]
  });

  submitted = false;
  loading = false;
  username = '';
  password = '';
  user: User[] = [];
  // user ?: User;

  constructor(  
    private formBuilder: FormBuilder,
    private userService: UserService,
    private router: Router
  ) { }

  ngOnInit() {
    const token = localStorage.getItem('token');
    if (token) {
      this.submitted = true;
    }
  }
  get f() { return this.registerForm.controls; }

  onSubmit() {
    this.submitted = true;

    if (this.registerForm.invalid) {
        return;
    }

    this.loading = true;
    // this.userService.register(this.registerForm.value);
    window.alert('Registration is success');
  }

  onRegister(): void {

    if (!this.username ||  !this.password || this.password.length < 5) {
      alert('Please, fill all lines!');
      this.username = '';
      this.password = '';
      return
    } 
    else{
        this.userService.signup(this.username, this.password).subscribe(res => {
          this.user.push(res);
        this.username = '';
        this.password = '';
          alert('You were successfully signed up. Now, please, log in');
          this.router.navigate(['/login']).then();
        });
    }
  }
}