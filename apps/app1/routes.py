from flask import Blueprint, render_template, request, jsonify
from . import app_bp
from .utils import compute_timer

@app_bp.route('/home')
def home():
	return 'Home de SpectraPlot'

@app_bp.route('/time', methods=['POST'])
def execute():
	data = request.get_json()
	initial = data['initial']
	final = data['final']

	time = compute_timer(initial, final)
	
	return jsonify(time)