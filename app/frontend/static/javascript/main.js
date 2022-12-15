let allOption = document.querySelectorAll(".option");
let allRules = document.querySelectorAll(".rule");
let board = document.querySelector(".board");
let section = document.getElementById("activtyFeld");
let textra = document.getElementById("txt1");
let ruleNum = 0;
let textBoard = ["<h1>Your input is:</h1>"];
let result = [];
let bractsNum = 0;
// ES6 Modules or TypeScript

// document.getElementsByName("activitiesOfThe1Rule")[0].value;

function insertText(elemID, text) {
	let elem = document.getElementById(elemID);
	elem.value = elem.value + " " + text;
}

addRuleToBoard = (array, rule) => {
	let text = "";
	switch (rule) {
		case 1:
			text = `<p><span>${array[0].value}</span> from different persons</p>`;
			textBoard.push(text);
			board.innerHTML = textBoard.join(" ");
			break;
		case 2:
			text = `<p><span>${array[0].value}</span> eventually <span>${array[1].value}</span></p>`;
			textBoard.push(text);
			board.innerHTML = textBoard.join(" ");
			break;
		case 3:
			text = `<p><span>${array[0].value}</span> next to <span>${array[1].value}</span> next to <span>${array[2].value}</span></p>`;
			textBoard.push(text);
			board.innerHTML = textBoard.join(" ");
			break;
		case 4:
			text = `<p><span>${array[0].value}</span> eventually <span>${array[1].value}</span> eventually <span>${array[2].value}</span> eventually <span>${array[3].value}</span></p>`;
			textBoard.push(text);
			board.innerHTML = textBoard.join(" ");
			break;
		case 5:
			text = `<p> Four eyes principle for ( <span>${array[0].value}</span>, <span>${array[1].value}</span>)}</p>`;
			textBoard.push(text);
			board.innerHTML = textBoard.join(" ");
			break;
		case 6:
			text = `<p><span>${array[0].value}</span> eventually <span>${array[1].value}</span> eventually <span>${array[2].value}</span></p>`;
			textBoard.push(text);
			board.innerHTML = textBoard.join(" ");
			break;

		default:
			board.innerHTML = " fehler";
			break;
	}
};

function addActivty(numOfActivties) {
	if (numOfActivties !== 0) {
		ruleNum++;

		let activty = document.getElementById(ruleNum);
		if (activty) removeAllInputsAt(activty);
		let newDiv = createDiv(ruleNum);
		newDiv.prepend(createText(ruleNum));
		createInputAt(numOfActivties, newDiv, ruleNum);
	}
}

findNumOfActivties = (element) => {
	switch (element) {
		case "A eventually B":
			return 2;
			break;
		case "Four eyes principle":
			return 5;
			break;
		case "Value different persons":
			return 1;
			break;
		case "A eventually B eventually C":
			return 6;
			break;
		case "A next to B next to C":
			return 3;
			break;
		case "A eventually B eventually C eventually D":
			return 4;
			break;
		default:
			return 0;
			break;
	}
};

hideRules = () => {
	document.querySelector(".filters").style.display = "none";
};

hideCom = () => {
	document.querySelector(".composition").style.display = "none";
};
showCom = () => {
	document.querySelector(".composition").style.display = "inline-block";
};

showRules = () => {
	document.querySelector(".filters").style.display = "inline-block";
	document.querySelector(".composition").style.display = "none";
};

allOption.forEach((element) => {
	element.addEventListener("click", () => {
		let buttonRule = element.innerText;
		result.push(element.value);
		backBtn.disabled = false;
		insertText("txt1", element.value);

		textra.value = result.join(" ");
		// addRuleToBoard(buttonRule);
		let rule = findNumOfActivties(buttonRule);
		if (rule === 5) rule = 2;
		if (rule === 6) rule = 3;
		addActivty(rule);
		if (!element.classList.contains("bracts")) {
			if (element.classList.contains("rule")) {
				hideRules();
				hideCom();
			} else {
				showRules();
				hideCom();
			}
		}
		if (
			element.classList.contains("bracts") ||
			element.classList.contains("or")
		) {
			textBoard.push(buttonRule);
			board.innerHTML = textBoard.join(" ");
			if (buttonRule == "(") bractsNum++;
			if (buttonRule == ")") bractsNum--;
		}
	});
});

function createDiv(name) {
	var newDiv = document.createElement("div");
	newDiv.id = name;
	newDiv.className = "activtyFeld";
	if (name == "first") section.prepend(newDiv);
	else section.append(newDiv);

	return newDiv;
}

function createText(ruleNum) {
	let text = document.createElement("h3");
	text.innerHTML = `Now choose the activities of the ${ruleNum} LTL rule:`;
	return text;
}

function createElementText(placeholder, ruleNum) {
	let activty = document.createElement("input");
	activty.required = true;
	activty.className = "activityInput";
	activty.type = "text";
	activty.name = `activitiesOfThe${ruleNum}Rule`;
	activty.placeholder = `activity ${placeholder}`;
	return activty;
}

function createInputAt(numOfActivties, place, ruleNum) {
	for (let index = 0; index < numOfActivties; index++) {
		let chr = String.fromCharCode(65 + index);
		let elm = createElementText(chr, ruleNum);
		elm.addEventListener("input", stateHandle);
		place.append(elm);
	}
	let btn = document.createElement("button");
	btn.id = "btn_" + ruleNum;
	let array = document.getElementsByName(`activitiesOfThe${ruleNum}Rule`);
	btn.innerHTML = "fill the activties";
	btn.className = "button";
	btn.type = "button";
	btn.disabled = true;
	btn.onclick = function () {
		addRuleToBoard(array, numOfActivties);
		showCom();
		document.getElementById(ruleNum).style.display = "none";
	};
	document.getElementById(ruleNum).children[1].focus();

	place.append(btn);
}

function stateHandle() {
	let array = document.getElementsByName(this.name);
	let btn = this.parentElement.lastElementChild;

	let empty = false;
	for (let index = 0; index < array.length; index++) {
		if (array[index].value === "") {
			empty = true;
			btn.disabled = true;
			btn.innerHTML = "fill the activties";
		}
	}
	if (!empty) {
		btn.disabled = false;
		btn.innerHTML = "Next";
	}
}

function removeAllInputsAt(place) {
	place.remove();
}

let restBn = document.getElementById("reset");
restBn.addEventListener("click", () => {
	section.innerHTML = "";
	board.innerHTML = "<h1>Your input is:</h1>";
	hideCom();
	showRules();
	ruleNum = 0;
	textBoard = ["<h1>Your input is:</h1>"];
	result = [];
	bractsNum = 0;
	textra.value = result.join(" ");
});

let backBtn = document.getElementById("back");
backBtn.addEventListener("click", () => {
	let lastEntry = result[result.length - 1];
	if (lastEntry == "LTL_Or" || lastEntry == "LTL_And") {
		deletLastEntry();
		showCom();
		hideRules();
	} else if (lastEntry == ")") {
		bractsNum++;
		deletLastEntry();
	} else if (lastEntry == "(") {
		bractsNum--;
		deletLastEntry();
	} else {
		hideCom();
		showRules();
		deletLastEntry();

		document.getElementById(ruleNum).remove();
		ruleNum--;
	}
	if (ruleNum < 1 && result.length == 0) {
		backBtn.disabled = true;
	}
});
function deletLastEntry() {
	result.pop();
	textBoard.pop();
	board.innerHTML = textBoard.join(" ");
	textra.value = result.join(" ");
}

let startBtn = document.getElementById("start");
startBtn.addEventListener("click", (event) => {
	let text = document.getElementById("txt1").value;
	if (text.length < 7) {
		swal("error!", "You have to choose an activity first", "error");

		event.preventDefault();
	}
	if (bractsNum > 0) {
		swal("check brackets!", `you have ${bractsNum} " ( " too many`, "warning");
		event.preventDefault();
	}
	if (bractsNum < 0) {
		swal("check brackets!", `you have ${-bractsNum} " ) " too many`, "warning");
		event.preventDefault();
	}
	let lastEntry = result[result.length - 1];
	if (lastEntry == "LTL_Or" || lastEntry == "LTL_And") {
		swal("check input!", "you have to choose another activity", "warning");
		event.preventDefault();
	}
});
