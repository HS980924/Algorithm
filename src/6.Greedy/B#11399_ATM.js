// Upload BOJ Silver-4 Greedy & Sort ATM

const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

let input = [];

const solution = (n, times) => {
    times.sort((a,b) => {
        return a-b;
    });

    let answer = 0
    let before = 0

    times.forEach(time=>{
        answer += time + before;
        before += time;
    });

    return answer;
}

rl.on('line',(line)=>{
    input.push(line);
});
rl.on('close',()=>{
    let N = parseInt(input[0]);
    let times = input[1].split(' ').map(el => parseInt(el));
    console.log(solution(N, times));
    process.exit();
})


// const readline = require('readline');

// const rl = readline.createInterface({
//     input: process.stdin,
//     output: process.stdout,
// });

// let cnt = 0;
// let N;
// let times = []

// const solution = (n, times) => {
//     times.sort();

//     let answer = 0
//     let before = 0

//     times.forEach(time=>{
//         answer += time + before;
//         before += time;
//     });

//     return answer;
// }

// rl.on('line',(line)=>{
//     if(cnt == 0){
//         N = parseInt(line);
//     }
//     else{
//         times = line.split(' ').map(el => parseInt(el));
//     }
//     cnt++;
    
//     //한 줄씩 입력 받은 후 실행할 코드
//     //입력된 값은 line에 저장
//     if (cnt == 2){
//         rl.close(); // 필수 close가 없으면 입력을 무한히 받는다.
//     }   
// });
// rl.on('close',()=>{
//     //입력이 끝난 후 실행할 코드
    

//     console.log(solution(N, times));
//     process.exit();
// })