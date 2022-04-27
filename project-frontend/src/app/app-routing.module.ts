import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {HomeComponent} from './home/home.component';
import {RecipeDetailComponent} from './recipe-detail/recipe-detail.component';
import {MainPageComponent} from './main-page/main-page.component';
import {AboutComponent} from './about/about.component';
import {LoginComponent} from './login/login.component';
import {SignupComponent} from './signup/signup.component';
import {RegistrationComponent } from './registration/registration.component';

const routes: Routes = [
  {path: 'recipes', component: HomeComponent},
  {path: 'recipes/:id', component: RecipeDetailComponent},
  {path: 'home', component: MainPageComponent},
  {path: 'about', component: AboutComponent},
  {path: 'login', component: LoginComponent},
  // {path: 'signup', component: SignupComponent},
  {path: 'register', component: RegistrationComponent},
  {path: '', redirectTo: 'home', pathMatch: 'full'}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
