let detail: string = "hoge";
// :の後に型名を指定（指定がない場合も初期値で決定）
// anyにするとなんでも受け入れちゃう
detail = "foo";
// detail = 100; ←エラーになる
let nums: number = 100;
nums = 0xFF;  //16進数（x）
nums = 0o666;  //8進数（o）
nums = 0b10111001; //2進数(b)
nums = 3E5; //指数？

let mail: string = "hogehoge@gmail.com";
let msg: string = `バッククォート（shift+@）で囲うと
改行とかの処理を勝手にしてくれる上に
変数をそのまま埋め込めるよ！メールはこちら→${mail}` 

function show(result: string){
    return `${result}はstring型です`;
};
// console.log(show(100)); ←数値型を渡すと当然エラー
console.log(show(<any>100));  //anyかstring型にしちゃう
console.log(show("100" as string));  //as 型名 でもおｋ

const DATA = [1, 2, 3];  //constは定数の宣言（大文字にすることが多いよ
// DATA = [4, 5, 6]; 再代入しようとするとエラー
DATA[0] = 10;  // 中身の要素だけ書き換えはできる！

let data: string[] = ["Java", "Python", "PHP"]; 
// 配列のときは型名の後に[]をつけないとダメだよ！
let data2: string[][] = [["Java", "Python", "PHP"], ["JavaScript", "HTML", "CSS"]];
// 入れ子にするときは次元の数だけ[]を指定！
// new Array(要素数)or(要素, 要素…)でも定義できるけど扱いづらい

let obj: {[index: string]: string;} = {
// 連想配列（Pythonでいうところの辞書）indexの部分はほかの名前でもいいよ
    "usa":"usako",
    "kato":"kato",
    "mya":"myako"
};
console.log(obj.usa);
console.log(obj["usa"]);
