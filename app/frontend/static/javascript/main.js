let allOption = document.querySelectorAll(".option");
let allRules = document.querySelectorAll(".rule");
let board = document.querySelector(".board");
let section = document.getElementById("activtyFeld");
let textra = document.getElementById("txt1");
let ruleNum = 0;
let textBoard = ["<h1>Your input is:</h1>"];
let result = [];
let bractsNum = 0;
let lastNextButton;
// ES6 Modules or TypeScript

function insertText(elemID, text) {
	let elem = document.getElementById(elemID);
	elem.value = elem.value + " " + text;
}

/*
	Add selected rules to the board.
*/
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

/*
	Match the selected LTL Rules with the corresponding numbers.
*/
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
		backBtn.disabled = false;
		// addRuleToBoard(buttonRule);
		let rule = findNumOfActivties(buttonRule);
		if (rule === 5) rule = 2;
		if (rule === 6) rule = 3;
		addActivty(rule);
		// if bracts are not selected
		if (!element.classList.contains("bracts")) {
			// if any rule is selected
			if (element.classList.contains("rule")) {
				hideRules();
				hideCom();
			} else {
				showRules();
				hideCom();
			}
		}
		if (element.classList.contains("or")) {
			textBoard.push(buttonRule);
			board.innerHTML = textBoard.join(" ");
		}
		if (element.classList.contains("bracts")) {
			if (buttonRule == "(") {
				bractsNum++;
				textBoard.push(buttonRule);
				board.innerHTML = textBoard.join(" ");
			}else if (buttonRule == ")" && bractsNum > 0) {
				bractsNum--;
				textBoard.push(buttonRule);
				board.innerHTML = textBoard.join(" ");
			} else {
				swal(
					"check brackets!",
					`you have to open " ( " frist`,
					"warning"
				);
				return;
			}
		}
		result.push(element.value);
		insertText("txt1", element.value);
		textra.value = result.join(" ");
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

/*
	numOfActivties: the number of actives required for the corresponding LTL Rule,
	ruleNum: the number of LTL Rules,
	This function is used to receive the activitives.
*/
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
		document.getElementById("NumberOfRules").value = ruleNum;
	};
	document.getElementById(ruleNum).children[1].focus();

	place.append(btn);
}

function stateHandle() {
	let array = document.getElementsByName(this.name);
	let btn = this.parentElement.lastElementChild;
	lastNextButton = btn;
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

activtyfildsDisply = () => {
	let hiden = true;

	let activtyfilds = document.getElementsByClassName("activtyFeld");
	for (let index = 0; index < activtyfilds.length; index++) {
		if (activtyfilds[index].style.display !== "none") hiden = false;
	}
	return hiden;
}

let backBtn = document.getElementById("back");
backBtn.addEventListener("click", () => {
	let lastEntry = result[result.length - 1];
	if (lastEntry == "LTL_Or" || lastEntry == "LTL_And") {
		deletLastEntry();
		showCom();
		hideRules();
	} else if (lastEntry == "LTL_RB") {
		bractsNum++;
		deletLastEntry();
	} else if (lastEntry == "LTL_LB") {
		bractsNum--;
		deletLastEntry();
	} else if (activtyfildsDisply()) {
		hideCom();
		showRules();
		deletLastEntry();
		document.getElementById(ruleNum).remove();
		ruleNum--;
	} else {
		hideCom();
		showRules();
		result.pop();
		board.innerHTML = textBoard.join(" ");
		textra.value = result.join(" ");
		document.getElementById(ruleNum).remove();
		ruleNum--;
	}
	if (ruleNum < 1 && result.length == 0) {
		textBoard = ["<h1>Your input is:</h1>"];
		board.innerHTML = "<h1>Your input is:</h1>";
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
	let lastElemStat = document.getElementById(ruleNum).style.display;
	if (lastElemStat !== "none") lastNextButton.click();
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
	let lastEntry = lastNoneBractsElment();
	if (lastEntry == "LTL_Or" || lastEntry == "LTL_And") {
		swal("check input!", "you have to choose another activity", "warning");
		event.preventDefault();
	}
});

function lastNoneBractsElment() {
	let copy = result.map((x) => x);
	let lastEntry = copy[copy.length - 1];
	while (lastEntry == "LTL_RB" || lastEntry == "LTL_LB") {
		copy.pop();
		lastEntry = copy[copy.length - 1];
	}
	return lastEntry;
	
}

let download_button = document.getElementById("result");
download_button.addEventListener("click", () => {
	download_button.style.display = "none";
});

