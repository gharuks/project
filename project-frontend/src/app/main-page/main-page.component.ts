import { Component, OnInit } from '@angular/core';
import {RecipesService} from '../recipes.service';
import {Recipe, Categories} from '../models';

@Component({
  selector: 'app-main-page',
  templateUrl: './main-page.component.html',
  styleUrls: ['./main-page.component.css']
})
export class MainPageComponent implements OnInit {
  categories: Categories[] = [];
  
  constructor(private recipesService: RecipesService,) { }

  ngOnInit(): void {
    this.getCategories();
  }

  getCategories():void {
    this.recipesService.getCategories().subscribe(categories => this.categories = this.categories);
  }

}
