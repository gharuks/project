import {Injectable} from '@angular/core';
// import {RECIPES} from './recipes';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {Observable, of} from 'rxjs';
import {Recipe, AuthToken, Ingredient, Categories} from './models';
import {MessageService} from './message.service';

@Injectable({
  providedIn: 'root'
})
export class RecipesService {
  BASE_URl = 'http://localhost:8000';
  httpHeaders = new HttpHeaders({'Content-Type': 'application/json'});
  constructor(private messageService: MessageService, private http: HttpClient) { }
  
  getRecipes(): Observable<Recipe[]>{
    return this.http.get<Recipe[]>(`${this.BASE_URl}/recipes/`);
  }

  putRecipes(recipe : Recipe): Observable<any>{
    return this.http.put<any>(`${this.BASE_URl}/recipes/${recipe.id}`, recipe);
  }

  getRecipe(id: number): Observable<Recipe>{
    return this.http.get<Recipe>(`${this.BASE_URl}/recipes/${id}`);
  }

  getCategories(): Observable<Categories[]>{
    return this.http.get<Categories[]>(`${this.BASE_URl}/categories/`);
  }

  getIngredient(id: number): Observable<Ingredient>{
    return this.http.get<Ingredient>(`${this.BASE_URl}/recipes/${id}/ingredients/`);
  }

  addRecipe(recipe: Recipe): Observable<any> {
    return this.http.post<any>(`${this.BASE_URl}/recipes/`, recipe, {headers: this.httpHeaders});
  }

  deleteProduct(recipe: Recipe): Observable<any> {
    let pk = recipe.id;
    return this.http.delete<any>(`${this.BASE_URl}/recipes/${pk}`);
  }
}
