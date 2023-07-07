// Upload BOG Silver-1 BFS 숨바꼭질

// const readline = require('readline');

// const rl = readline.createInterface({
//     input:process.stdin,
//     output:process.stdout,
// });

// let input = []

// const bfs = (n,k) => {
//     q = new Queue();
//     maps = Array.from({length: 100001},()=>0);
    
//     q.add(n)
//     maps[n] = 1

//     while (q.size()){
//         x = q.popleft()

//         if (x == k){
//             console.log(maps[k]-1);
//             break;
//         }

//         tmp = [x-1, x+1, x*2];

//         tmp.forEach(nx => {
//             if (0 <= nx < 100001 && !maps[nx]){
//                 maps[nx] = maps[x]+1;
//                 q.add(nx);
//             }
//         });
//     }

// }

// class Queue {
//     constructor() {
//         this.storage = {};
//         this.front = 0;
//         this.rear = 0;
//     }
    
//     size() {
//         if (this.storage[this.rear] === undefined) {
//             return 0;
//         } else {
//             return this.rear - this.rear + 1;
//         }
//     }
    
//     add(value) {
//         if (this.size() === 0) {
//             this.storage['0'] = value;
//         } else {
//             this.rear += 1;
//             this.storage[this.rear] = value;
//         }
//     }
    
//     popleft() {
//         let temp;
//         if (this.front === this.rear) {
//             temp = this.storage[this.front];
//             delete this.storage[this.front];
//             this.front = 0;
//             this.rear = 0;
//         } else {
//             temp = this.storage[this.front];
//             delete this.storage[this.front];
//             this.front += 1;
//         }
//         return temp;
//     }
// }

// rl.on('line',(line)=>{
//     input.push(line);
// });
// rl.on('close',()=>{
//     let loc = input[0].split(' ').map(el => parseInt(el));
//     bfs(loc[0],loc[1]);
//     process.exit();
// })


// const readline = require('readline');

// const solution = (input) => {
//     const [N, K] = input.split(" ").map(Number);
    
//     const bfs = (n,k) =>{
//         const queue = [[n,0]];
//         const visit = Array.from({length:100001},()=>0);
//         visit[n] = 1;

//         while (queue.length){
//             const [x, time] = queue.shift();
//             if (x == k){
//                 console.log(time);
//                 break;
//             }
//             for(nx of [x-1, x+1, x*2]){
//                 if( 0 <= nx && nx < 100001 && !visit[nx]){
//                     visit[nx] = 1;
//                     queue.push([nx,time+1])
//                 }
//             }
//         }
//     }

//     bfs(N, K);
// }

// readline.createInterface({
//     input: process.stdin,
//     output: process.stdout,
// }).on('line',(line)=>{
//     solution(line);
// }).on('close',()=>{
//     process.exit();
// })

// const sol = (input) => {
//     const [N, K] = input.split(" ").map(Number);
//     const visit = Array.from({ length: 100100 }, () => 0);
  
//     function bfs(N) {
//       const queue = [];
//       queue.push([N, 0]);
//       visit[N] = 1;
//       while (queue.length) {
//         const [cur, time] = queue.shift();
//         if (cur === K) return time;
//         for (next of [cur - 1, cur + 1, cur * 2]) {
//           if (!visit[next] && next >= 0 && next <= 100000) {
//             visit[next] = 1;
//             queue.push([next, time + 1]);
//           }
//         }
//       }
//     }
//     return bfs(N);
//   };
  
//   require("readline")
//     .createInterface(process.stdin, process.stdout)
//     .on("line", (line) => {
//       console.log(sol(line));
//     })
//     .on("close", () => {
//       process.exit();
//     });