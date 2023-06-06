///javascript 기초문법 정의(https://www.youtube.com/watch?v=hcdyyzDQ2O8)

//웬만하면 상수선언. 필요할 때 변수로 
const hi = '안녕하세요';
console.log(hi);

//반복문
const lt = [1,3,5];
for (i in lt){
    console.log('${i}임메');
}

//반복문2
for (let x=0;x<10;x++){
    console.log(x+1);
};

//반복문, 조건문
while (true) {
    if (length.lt === 3) {
        console.log('z')    
        break
    } else if(length.lt != 3) {
        continue
    } else {

    };
};

//함수, 인자 디폴트밸류 설정,  
function sum(a, b= 0){
    console.log(arguments) //args를 배열형태로 저장하고 있음. 몇개가 함수에 소환되던 간에.
    return a+b
};
console.log(sum(10));
console.log(sum(1,2,3,4,5,6))