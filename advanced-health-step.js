// CODE À INSÉRER DANS index.html AVANT LA LIGNE 993 (if (step === 'wellbeing'))

// NOUVEAU : PAGE SANTÉ AVANCÉE (15 QUESTIONS)
if (step === 'advanced-health') {
    return React.createElement('div', { className: 'min-h-screen bg-gradient-to-br from-green-50 via-white to-blue-50 py-8 px-4' },
        React.createElement('div', { className: 'max-w-3xl mx-auto' },
            React.createElement('div', { className: 'text-center mb-8' },
                React.createElement('div', { className: 'inline-block bg-gradient-to-r from-green-600 to-blue-600 p-4 rounded-2xl mb-4' },
                    React.createElement('i', { 'data-lucide': 'activity', className: 'w-16 h-16 text-white' })
                ),
                React.createElement('h1', { className: 'text-4xl font-bold text-gray-800 mb-4' }, 'Santé Approfondie'),
                React.createElement('p', { className: 'text-xl text-gray-600' }, 'Quelques questions supplémentaires pour un diagnostic précis')
            ),

            React.createElement('div', { className: 'bg-white rounded-3xl shadow-2xl p-8' },
                // Section 1: Santé Cardiovasculaire
                React.createElement('div', { className: 'mb-8' },
                    React.createElement('h2', { className: 'text-2xl font-bold text-gray-800 mb-6 flex items-center' },
                        React.createElement('span', { className: 'bg-red-600 text-white w-8 h-8 rounded-full flex items-center justify-center mr-3' }, '♥'),
                        'Santé Cardiovasculaire'
                    ),

                    React.createElement('div', { className: 'space-y-6' },
                        // Q1: Tension artérielle
                        React.createElement('div', null,
                            React.createElement('label', { className: 'block text-gray-700 font-semibold mb-3' }, 'Votre tension artérielle'),
                            React.createElement('select', {
                                name: 'bloodPressure',
                                value: advancedHealthData.bloodPressure,
                                onChange: handleAdvancedHealthChange,
                                className: 'w-full px-4 py-3 border-2 border-gray-200 rounded-lg focus:border-green-500 focus:outline-none'
                            },
                                React.createElement('option', { value: '1' }, 'Normale (< 120/80)'),
                                React.createElement('option', { value: '2' }, 'Pré-hypertension (120-139/80-89)'),
                                React.createElement('option', { value: '3' }, 'Hypertension légère (140-159/90-99)'),
                                React.createElement('option', { value: '4' }, 'Hypertension sévère (≥160/100)'),
                                React.createElement('option', { value: '5' }, 'Je ne sais pas')
                            )
                        ),

                        // Q2: Fréquence cardiaque
                        React.createElement('div', null,
                            React.createElement('label', { className: 'block text-gray-700 font-semibold mb-3' },
                                'Fréquence cardiaque au repos (bpm)'
                            ),
                            React.createElement('input', {
                                type: 'range',
                                name: 'restingHeartRate',
                                min: '40',
                                max: '100',
                                value: advancedHealthData.restingHeartRate,
                                onChange: handleAdvancedHealthChange,
                                className: 'w-full'
                            }),
                            React.createElement('div', { className: 'flex justify-between text-sm text-gray-600 mt-2' },
                                React.createElement('span', null, '40'),
                                React.createElement('span', { className: 'font-bold text-green-600' }, advancedHealthData.restingHeartRate + ' bpm'),
                                React.createElement('span', null, '100')
                            )
                        ),

                        // Q3: Antécédents familiaux
                        React.createElement('div', null,
                            React.createElement('label', { className: 'block text-gray-700 font-semibold mb-3' },
                                'Maladies cardiaques dans votre famille proche ?'
                            ),
                            React.createElement('div', { className: 'grid grid-cols-3 gap-4' },
                                React.createElement('label', {
                                    className: `flex items-center justify-center p-4 border-2 rounded-lg cursor-pointer transition ${advancedHealthData.familyHistory === 'no' ? 'border-green-500 bg-green-50' : 'border-gray-200'}`
                                },
                                    React.createElement('input', {
                                        type: 'radio',
                                        name: 'familyHistory',
                                        value: 'no',
                                        checked: advancedHealthData.familyHistory === 'no',
                                        onChange: handleAdvancedHealthChange,
                                        className: 'mr-2'
                                    }),
                                    React.createElement('span', { className: 'font-semibold' }, 'Non')
                                ),
                                React.createElement('label', {
                                    className: `flex items-center justify-center p-4 border-2 rounded-lg cursor-pointer transition ${advancedHealthData.familyHistory === 'after70' ? 'border-yellow-500 bg-yellow-50' : 'border-gray-200'}`
                                },
                                    React.createElement('input', {
                                        type: 'radio',
                                        name: 'familyHistory',
                                        value: 'after70',
                                        checked: advancedHealthData.familyHistory === 'after70',
                                        onChange: handleAdvancedHealthChange,
                                        className: 'mr-2'
                                    }),
                                    React.createElement('span', { className: 'font-semibold text-sm' }, 'Après 70 ans')
                                ),
                                React.createElement('label', {
                                    className: `flex items-center justify-center p-4 border-2 rounded-lg cursor-pointer transition ${advancedHealthData.familyHistory === 'before60' ? 'border-red-500 bg-red-50' : 'border-gray-200'}`
                                },
                                    React.createElement('input', {
                                        type: 'radio',
                                        name: 'familyHistory',
                                        value: 'before60',
                                        checked: advancedHealthData.familyHistory === 'before60',
                                        onChange: handleAdvancedHealthChange,
                                        className: 'mr-2'
                                    }),
                                    React.createElement('span', { className: 'font-semibold text-sm' }, 'Avant 60 ans')
                                )
                            )
                        )
                    )
                ),

                // Section 2: Santé Digestive
                React.createElement('div', { className: 'mb-8' },
                    React.createElement('h2', { className: 'text-2xl font-bold text-gray-800 mb-6 flex items-center' },
                        React.createElement('span', { className: 'bg-orange-600 text-white w-8 h-8 rounded-full flex items-center justify-center mr-3' }, '🍎'),
                        'Santé Digestive'
                    ),

                    React.createElement('div', { className: 'space-y-6' },
                        // Q4: Digestion
                        React.createElement('div', null,
                            React.createElement('label', { className: 'block text-gray-700 font-semibold mb-3' },
                                'Qualité de votre digestion'
                            ),
                            React.createElement('input', {
                                type: 'range',
                                name: 'digestion',
                                min: '1',
                                max: '5',
                                value: advancedHealthData.digestion,
                                onChange: handleAdvancedHealthChange,
                                className: 'w-full'
                            }),
                            React.createElement('div', { className: 'flex justify-between text-sm text-gray-600 mt-2' },
                                React.createElement('span', null, 'Problèmes'),
                                React.createElement('span', null, 'Excellente')
                            )
                        ),

                        // Q5: Fibres
                        React.createElement('div', null,
                            React.createElement('label', { className: 'block text-gray-700 font-semibold mb-3' },
                                'Consommation d\'aliments riches en fibres'
                            ),
                            React.createElement('input', {
                                type: 'range',
                                name: 'fiber',
                                min: '1',
                                max: '5',
                                value: advancedHealthData.fiber,
                                onChange: handleAdvancedHealthChange,
                                className: 'w-full'
                            }),
                            React.createElement('div', { className: 'flex justify-between text-sm text-gray-600 mt-2' },
                                React.createElement('span', null, 'Rarement'),
                                React.createElement('span', null, 'Quotidien')
                            )
                        )
                    )
                ),

                // Section 3: Mobilité & Flexibilité
                React.createElement('div', { className: 'mb-8' },
                    React.createElement('h2', { className: 'text-2xl font-bold text-gray-800 mb-6 flex items-center' },
                        React.createElement('span', { className: 'bg-blue-600 text-white w-8 h-8 rounded-full flex items-center justify-center mr-3' }, '🤸'),
                        'Mobilité & Flexibilité'
                    ),

                    React.createElement('div', { className: 'space-y-6' },
                        // Q6: Flexibilité
                        React.createElement('div', null,
                            React.createElement('label', { className: 'block text-gray-700 font-semibold mb-3' },
                                'Pouvez-vous toucher vos orteils sans plier les genoux ?'
                            ),
                            React.createElement('div', { className: 'grid grid-cols-3 gap-4' },
                                React.createElement('label', {
                                    className: `flex items-center justify-center p-4 border-2 rounded-lg cursor-pointer transition ${advancedHealthData.flexibility === 'easy' ? 'border-green-500 bg-green-50' : 'border-gray-200'}`
                                },
                                    React.createElement('input', {
                                        type: 'radio',
                                        name: 'flexibility',
                                        value: 'easy',
                                        checked: advancedHealthData.flexibility === 'easy',
                                        onChange: handleAdvancedHealthChange,
                                        className: 'mr-2'
                                    }),
                                    React.createElement('span', { className: 'font-semibold' }, 'Facilement')
                                ),
                                React.createElement('label', {
                                    className: `flex items-center justify-center p-4 border-2 rounded-lg cursor-pointer transition ${advancedHealthData.flexibility === 'hard' ? 'border-yellow-500 bg-yellow-50' : 'border-gray-200'}`
                                },
                                    React.createElement('input', {
                                        type: 'radio',
                                        name: 'flexibility',
                                        value: 'hard',
                                        checked: advancedHealthData.flexibility === 'hard',
                                        onChange: handleAdvancedHealthChange,
                                        className: 'mr-2'
                                    }),
                                    React.createElement('span', { className: 'font-semibold' }, 'Difficilement')
                                ),
                                React.createElement('label', {
                                    className: `flex items-center justify-center p-4 border-2 rounded-lg cursor-pointer transition ${advancedHealthData.flexibility === 'impossible' ? 'border-red-500 bg-red-50' : 'border-gray-200'}`
                                },
                                    React.createElement('input', {
                                        type: 'radio',
                                        name: 'flexibility',
                                        value: 'impossible',
                                        checked: advancedHealthData.flexibility === 'impossible',
                                        onChange: handleAdvancedHealthChange,
                                        className: 'mr-2'
                                    }),
                                    React.createElement('span', { className: 'font-semibold' }, 'Impossible')
                                )
                            )
                        ),

                        // Q7: Équilibre
                        React.createElement('div', null,
                            React.createElement('label', { className: 'block text-gray-700 font-semibold mb-3' },
                                'Équilibre sur un pied pendant 30 secondes'
                            ),
                            React.createElement('div', { className: 'grid grid-cols-3 gap-4' },
                                React.createElement('label', {
                                    className: `flex items-center justify-center p-4 border-2 rounded-lg cursor-pointer transition ${advancedHealthData.balance === 'yes' ? 'border-green-500 bg-green-50' : 'border-gray-200'}`
                                },
                                    React.createElement('input', {
                                        type: 'radio',
                                        name: 'balance',
                                        value: 'yes',
                                        checked: advancedHealthData.balance === 'yes',
                                        onChange: handleAdvancedHealthChange,
                                        className: 'mr-2'
                                    }),
                                    React.createElement('span', { className: 'font-semibold' }, 'Oui')
                                ),
                                React.createElement('label', {
                                    className: `flex items-center justify-center p-4 border-2 rounded-lg cursor-pointer transition ${advancedHealthData.balance === 'hard' ? 'border-yellow-500 bg-yellow-50' : 'border-gray-200'}`
                                },
                                    React.createElement('input', {
                                        type: 'radio',
                                        name: 'balance',
                                        value: 'hard',
                                        checked: advancedHealthData.balance === 'hard',
                                        onChange: handleAdvancedHealthChange,
                                        className: 'mr-2'
                                    }),
                                    React.createElement('span', { className: 'font-semibold' }, 'Avec difficulté')
                                ),
                                React.createElement('label', {
                                    className: `flex items-center justify-center p-4 border-2 rounded-lg cursor-pointer transition ${advancedHealthData.balance === 'no' ? 'border-red-500 bg-red-50' : 'border-gray-200'}`
                                },
                                    React.createElement('input', {
                                        type: 'radio',
                                        name: 'balance',
                                        value: 'no',
                                        checked: advancedHealthData.balance === 'no',
                                        onChange: handleAdvancedHealthChange,
                                        className: 'mr-2'
                                    }),
                                    React.createElement('span', { className: 'font-semibold' }, 'Non')
                                )
                            )
                        ),

                        // Q8: Douleurs articulaires
                        React.createElement('div', null,
                            React.createElement('label', { className: 'block text-gray-700 font-semibold mb-3' },
                                'Fréquence des douleurs articulaires'
                            ),
                            React.createElement('input', {
                                type: 'range',
                                name: 'jointPain',
                                min: '1',
                                max: '5',
                                value: advancedHealthData.jointPain,
                                onChange: handleAdvancedHealthChange,
                                className: 'w-full'
                            }),
                            React.createElement('div', { className: 'flex justify-between text-sm text-gray-600 mt-2' },
                                React.createElement('span', null, 'Jamais'),
                                React.createElement('span', null, 'Quotidien')
                            )
                        )
                    )
                ),

                // Section 4: Environnement (questions simplifiées pour gagner de la place)
                React.createElement('div', { className: 'mb-8' },
                    React.createElement('h2', { className: 'text-2xl font-bold text-gray-800 mb-6 flex items-center' },
                        React.createElement('span', { className: 'bg-green-600 text-white w-8 h-8 rounded-full flex items-center justify-center mr-3' }, '🌍'),
                        'Environnement & Habitudes'
                    ),

                    React.createElement('div', { className: 'space-y-6' },
                        // Q9-13: Questions rapides
                        React.createElement('div', null,
                            React.createElement('label', { className: 'block text-gray-700 font-semibold mb-3' },
                                'Temps d\'écran quotidien (hors travail)'
                            ),
                            React.createElement('input', {
                                type: 'range',
                                name: 'screenTime',
                                min: '0',
                                max: '12',
                                value: advancedHealthData.screenTime,
                                onChange: handleAdvancedHealthChange,
                                className: 'w-full'
                            }),
                            React.createElement('div', { className: 'flex justify-between text-sm text-gray-600 mt-2' },
                                React.createElement('span', null, '0h'),
                                React.createElement('span', { className: 'font-bold' }, advancedHealthData.screenTime + 'h'),
                                React.createElement('span', null, '12h')
                            )
                        ),

                        React.createElement('div', null,
                            React.createElement('label', { className: 'block text-gray-700 font-semibold mb-3' },
                                'Activités intellectuelles (lecture, puzzles, apprentissage)'
                            ),
                            React.createElement('input', {
                                type: 'range',
                                name: 'cognitiveActivities',
                                min: '1',
                                max: '5',
                                value: advancedHealthData.cognitiveActivities,
                                onChange: handleAdvancedHealthChange,
                                className: 'w-full'
                            }),
                            React.createElement('div', { className: 'flex justify-between text-sm text-gray-600 mt-2' },
                                React.createElement('span', null, 'Rarement'),
                                React.createElement('span', null, 'Quotidien')
                            )
                        ),

                        React.createElement('div', null,
                            React.createElement('label', { className: 'block text-gray-700 font-semibold mb-3' },
                                'Qualité de votre mémoire'
                            ),
                            React.createElement('input', {
                                type: 'range',
                                name: 'memoryQuality',
                                min: '1',
                                max: '5',
                                value: advancedHealthData.memoryQuality,
                                onChange: handleAdvancedHealthChange,
                                className: 'w-full'
                            }),
                            React.createElement('div', { className: 'flex justify-between text-sm text-gray-600 mt-2' },
                                React.createElement('span', null, 'Mauvaise'),
                                React.createElement('span', null, 'Excellente')
                            )
                        )
                    )
                ),

                // Bouton Submit
                React.createElement('button', {
                    onClick: handleAdvancedSubmit,
                    className: 'w-full bg-gradient-to-r from-green-600 to-blue-600 hover:from-green-700 hover:to-blue-700 text-white text-xl font-bold py-4 rounded-xl transition transform hover:scale-105 shadow-lg'
                }, '🎯 Calculer Mon Âge Biologique Complet')
            )
        )
    );
}
