import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { User } from './user';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { catchError, map, shareReplay, tap } from 'rxjs/operators';
import { AuthToken } from './models';

@Injectable({
  providedIn: 'root'
})
export class UserService {
  
  BASE_URl = 'http://127.0.0.1:8000/';

  httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' })
  };

  constructor(
    private http: HttpClient,
  ) { }
  
  logged(): boolean{
    if (localStorage.getItem('token')){
      return true;
    }
    return false;
  }
  // getUsers(): Observable<User[]> {
  //   return this.http.get<User[]>( `${this.BASE_URl}/users`)
  // }
  
  // getUser(): Observable<User>{
  //   return this.http.get<User>(`${this.BASE_URl}/user`);
  // }

  login(username: string, password: string): Observable<AuthToken>{
    return this.http.post<AuthToken>(`${this.BASE_URl}login/`, {
      username,
      password
    });
  }

  signup(username: string, password: string): Observable<User> {
    return this.http.post<User>(this.BASE_URl + 'sign-up/', {username, password})
  }
  
}