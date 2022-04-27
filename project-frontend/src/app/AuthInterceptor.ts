import {HttpClient, HttpEvent, HttpHandler, HttpInterceptor, HttpRequest} from "@angular/common/http";
import {Observable} from "rxjs/internal/Observable";
import {Injectable} from "@angular/core";
import { User } from "./user";

@Injectable()
export class AuthInterceptor  implements HttpInterceptor {
  constructor(private http: HttpClient) {
  }

  intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {

    const token = localStorage.getItem('token');
    if (token){
      const authReq = req.clone({
        headers: req.headers.append('Authorization', `JWT ${token}`)
      });
      return next.handle(authReq);
    }

    return next.handle(req);
  }

  login(email:string, password:string ) {
    return this.http.post<User>('/api/login', {email, password})
        // this is just the HTTP call, 
        // we still need to handle the reception of the token
        // .shareReplay();
  }
}