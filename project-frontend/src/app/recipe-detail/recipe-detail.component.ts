import { Component, OnInit } from '@angular/core';
import {Ingredient, Recipe} from '../models';
import {ActivatedRoute} from '@angular/router';
import {RecipesService} from '../recipes.service';
import {Location} from "@angular/common";
import {INGREDIENTS} from "../ingredients";


@Component({
  selector: 'app-recipe-detail',
  templateUrl: './recipe-detail.component.html',
  styleUrls: ['./recipe-detail.component.css']
})
export class RecipeDetailComponent implements OnInit {
  recipe ?: Recipe;
  ingredient ?: Ingredient;
  // @ts-ignore
  id = +this.route.snapshot.paramMap.get('id');

  constructor(private route: ActivatedRoute,
              private location: Location,
              private recipesService: RecipesService) {

  }

    ngOnInit(): void {
      this.getRecipe();
      this.getIngredient();
    }
    
    getRecipe(): void {
      this.recipesService.getRecipe(this.id).subscribe(data => {
        this.recipe = data;
      });
    }

    getIngredient(): void{
      this.recipesService.getIngredient(this.id).subscribe(data => {
        this.ingredient = data;
      });
    }

    goBack(): void {
      this.location.back();
    }
    
  }

  
  // getRecipe(): void {
  //   this.route.paramMap.subscribe((params) => {
  //     const id = Number(params.get('id'));
  //     this.loaded = false;
  //     this.recipesService.getRecipe(id).subscribe((recipe) => {
  //       this.recipe = recipe;
  //       this.loaded = true;
  //     });
  //   });
  // }


// goBack(): void {
//     this.location.back();
//   }

