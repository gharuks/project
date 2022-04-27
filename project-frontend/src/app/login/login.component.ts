import { Component, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms';
import { from } from 'rxjs';
import {UserService} from '../user.service';
import {User} from '../user';
import { Location } from '@angular/common';
import {Router} from '@angular/router';
import {RecipesService} from '../recipes.service';
import { Recipe } from '../models';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})

export class LoginComponent implements OnInit {
  user ?: User;
  logged = false;
  username = '';
  password = '';
  name = localStorage.getItem('username');
  newname: String;
  newdescription: String;
  newtag: String;
  newimage: String;
  newlike: Number;
  newdislike: Number;
  loading : boolean = false;
  recipes : Recipe[] = [];


  ngOnInit() {
    const token = localStorage.getItem('token');
    if (token) {
      this.logged = true;
    }
    this.getRecipes();
  }

  constructor(private userService: UserService,
    private recipesService: RecipesService,
    private location: Location, 
    private router: Router) {
      this.newname = '',
      this.newdescription = '',
      this.newtag = '',
      this.newimage = '',
      this.newlike = 0,
      this.newdislike = 0
  }

  login() {
    this.userService.login(this.username, this.password).subscribe((data) => {
      console.log(data);
      localStorage.setItem('token', data.token);
      localStorage.setItem('username', this.username);
      this.logged = true;
      this.router.navigate(['/home']).then();
    });
  }
  
  logout() {
    this.logged = false;
    localStorage.removeItem('token');
    localStorage.removeItem('username');
  }
  goBack(): void {
    this.location.back();
  }

  getRecipes(): void {
    this.recipesService.getRecipes().subscribe(recipes => this.recipes = recipes);
  }

  addProduct() {
    const product = {
      name: this.newname,
      description : this.newdescription,
      tag : this.newtag,
      image: this.newimage,
      like : this.newlike,
      dislike : this.newdislike,
    };
    this.loading = false;
    this.recipesService.addRecipe(product as Recipe).subscribe((product) => {
      this.recipes.unshift(product);
      this.newname = '';
      this.newdescription = '';
      this.newtag = '';
      this.newimage = '';
      this.newlike = 0;
      this.newdislike = 0;
      this.loading = true;
    });
  }

  deleteProduct(recipe: Recipe) {
    this.recipesService.deleteProduct(recipe).subscribe(() => {
      // alert('deleted');
    });

  }
}