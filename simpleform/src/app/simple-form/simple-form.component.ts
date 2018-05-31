import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-simple-form',
  templateUrl: './simple-form.component.html',
  styleUrls: ['./simple-form.component.css']
})
export class SimpleFormComponent implements OnInit {
  text1;
  text2;
  result = '足し算しよう';
  // 通常時resultの中身
  addAndShow(): void {
    // クリック時に実行するやつ。 void の部分は型の宣言(省略可）
    let forResult = '半角数字のみで入力してね';
    let input1: number;
    let input2: number;

    input1 = Number(this.text1);
    input2 = Number(this.text2);

    if (!Number.isNaN(input1) && !Number.isNaN(input2)) {
      forResult = `${input1}+${input2}=${input1 + input2}`;
    }
    this.result = forResult;
    }
  constructor() { }

  ngOnInit() {
  }

}
