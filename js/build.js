const nwbuild=require("nw-builder");
const nw=new nwbuild({
	files:"./src/**",
    platforms:["win32"],
	flavor:"normal",
	buildDir:"./"
});
nw.on("log",console.log);
nw.build()
	.then(()=>console.log("done!"))
	.catch(e=>console.error(e));
