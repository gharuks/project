import { Component, OnInit } from '@angular/core';
import {Recipe, Categories} from '../models';
import {RecipesService} from '../recipes.service';
import {MessageService} from '../message.service';
// import {RECIPES} from '../recipes';


@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  recipes: Recipe[] = [];
  categories: Categories[] = [];
  name = localStorage.getItem('username');
  //@ts-ignore
  recipe: Recipe;
  constructor(private recipesService: RecipesService,
              private messageService: MessageService) {
  }

  ngOnInit(): void {
    this.getRecipes();
    // this.putRecipes();
  }

  getRecipes(): void {
    this.recipesService.getRecipes().subscribe(recipes => this.recipes = recipes);
  }

  putRecipes(): void{
    //@ts-ignore
    this.recipesService.putRecipes(recipe).subscribe(recipe => {console.log(this.recipe);});
  }

  likeItem(x : Recipe) {
    //@ts-ignore
    x.like = x.like + 1;
    this.putRecipes();
  }

  DislikeItem(x : Recipe){
    x.dislike += 1;
    this.putRecipes();
  }

  share(link: String, text: String) {
    window.open('https://telegram.me/share/url?url='+link, '_blank')
  }

  removeItem(id: number): void {
    this.recipes = this.recipes.filter(x => x.id !== id);
  }
  // getRecipes(): void {
  //   this.recipesService.getRecipes().subscribe((recipes) => {
  //     this.recipes = recipes;
  //   });
  // }
}
