import { User } from "./user";

export interface Recipe {
  name: string;
  id: number;
  author: User;
  description: string;
  tag: string;
  image: string;
  like: number;
  dislike: number;
}
export interface Ingredient {
  id: number;
  ing1: string;
  amount1: string;
  ing2: string;
  amount2: string;
  ing3: string;
  amount3: string;
  ing4: string;
  amount4: string;
  ing5: string;
  amount5: string;
  ing6: string;
  amount6: string;
  ing7: string;
  amount7: string;
  ing8: string;
  amount8: string;
  ing9: string;
  amount9: string;
  ing10: string;
  amount10: string;
  ing11: string;
  amount11: string;
  ing12: string;
  amount12: string;
  ing13: string;
  amount13: string;
  ing14: string;
  amount14: string;
  ing15: string;
  amount15: string;
  step1: string;
  step2: string;
  step3: string;
  step4: string;
  step5: string;
  step6: string;
  step7: string;
  step8: string;
  step9: string;
  step10: string;
}

export interface AuthToken {
  token: string;
}

// export interface User {
//   username: string;
//   password: string;
//   firstName: string;
//   lastName: string;
// }

export interface Categories{
  name: string
}
